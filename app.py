import gradio as gr
import asyncio
import time
import textwrap

# --- 1. CSS for Styling ---
app_css = """
/* General Styling */
.gradio-container { font-family: 'Inter', sans-serif; background-color: #f8fafc; }

/* Main Panel Styling */
.main-panel {
    background-color: white;
    border: 1px solid #e2e8f0;
    border-radius: 1rem;
    padding: 1.5rem;
    height: 100%;
}
.main-panel h2 {
    font-size: 1.25rem;
    font-weight: 600;
    color: #1e293b;
    margin-bottom: 1rem;
    display: flex;
    align-items: center;
}
.main-panel h2 i { margin-right: 0.75rem; color: #0891b2; }

/* Log Output Styling */
.log-output textarea {
    background-color: #0f172a !important;
    color: #e2e8f0 !important;
    font-family: monospace !important;
    font-size: 0.875rem !important;
    border-radius: 0.5rem !important;
}

/* Icon Styling */
.fa-spinner { animation: fa-spin 2s infinite linear; }
@keyframes fa-spin { 0% { transform: rotate(0deg); } 100% { transform: rotate(360deg); } }
"""

# --- 2. SIMULATED AGENT LOGIC ---
# This async generator function simulates the browser agent's execution.
# In a real application, you would replace this with calls to your actual Agent class.
async def run_browser_agent(task):
    """
    Simulates the step-by-step execution of the browser agent and yields log updates.
    """
    log_history = ""
    
    # Initial message
    log_history += "[INFO] Agent initialized.\n"
    yield log_history
    await asyncio.sleep(1)

    # Step 1: Planning
    log_history += f"[PLAN] Task received: '{task}'\n"
    log_history += "[PLAN] Steps: 1. Go to URL. 2. Search. 3. Sort. 4. Extract price.\n"
    yield log_history
    await asyncio.sleep(1.5)

    # Step 2: Navigation
    log_history += "[ACTION] Navigating to https://www.flipkart.com...\n"
    yield log_history
    await asyncio.sleep(2)
    log_history += "[OBSERVATION] Successfully landed on Flipkart homepage.\n"
    yield log_history
    await asyncio.sleep(1)

    # Step 3: Search
    log_history += "[ACTION] Finding search bar and typing 'laptop'...\n"
    yield log_history
    await asyncio.sleep(1.5)
    log_history += "[OBSERVATION] Search results for 'laptop' are now displayed.\n"
    yield log_history
    await asyncio.sleep(1)

    # Step 4: Sorting
    log_history += "[ACTION] Finding and clicking 'Sort by Rating' option...\n"
    yield log_history
    await asyncio.sleep(2)
    log_history += "[OBSERVATION] Products are now sorted by highest customer rating.\n"
    yield log_history
    await asyncio.sleep(1)

    # Step 5: Extraction
    log_history += "[ACTION] Identifying the first product in the list...\n"
    yield log_history
    await asyncio.sleep(1)
    log_history += "[ACTION] Extracting price information from the product details...\n"
    yield log_history
    await asyncio.sleep(1.5)
    
    # Final Result
    final_result = """
[RESULT] Task completed. Here is the price of the first item:

---
### Product: ASUS Vivobook 15
- **Price:** ₹54,990
- **Rating:** 4.8 Stars
---
    """
    log_history += final_result
    yield log_history


# --- 3. GRADIO UI LAYOUT ---
with gr.Blocks(css=app_css, theme=gr.themes.Soft()) as demo:
    gr.Markdown(
        textwrap.dedent("""
        # <i class="fas fa-robot" style="color:#0891b2;"></i> Web Automation Agent
        <p style="font-size:0.9rem; color:#475569;">Give the agent a task, and it will use a browser to complete it.</p>
        """)
    )
    
    with gr.Column(elem_classes=["main-panel"]):
        task_input = gr.Textbox(
            label="Task for the Agent",
            placeholder="e.g., Go to flipkart.com, search for laptop, sort by best rating...",
            lines=3
        )
        
        run_button = gr.Button("Run Agent", variant="primary")
        
        gr.Markdown('<h2><i class="fas fa-file-alt"></i> Agent Log & Output</h2>')
        
        log_output = gr.Textbox(
            label="Live Log",
            elem_classes=["log-output"],
            lines=20,
            interactive=False,
            autoscroll=True
        )

    # --- Event Listener ---
    run_button.click(
        fn=run_browser_agent,
        inputs=[task_input],
        outputs=[log_output]
    )


if __name__ == "__main__":
    # The queue() method is required for streaming outputs
    demo.queue()
    demo.launch(debug=True)
