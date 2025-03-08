from bs4 import BeautifulSoup

def update_div_content(html_file, div_id, new_content, output_file=None):
    """
    Load an HTML file and change the contents of a div with the specified ID.
    
    Parameters:
    html_file (str): Path to the HTML file
    div_id (str): ID of the div to modify
    new_content (str): New content to put in the div
    output_file (str): Path to save the modified HTML (if None, overwrites original)
    """
    # Load the HTML file
    with open(html_file, 'r', encoding='utf-8') as file:
        html_content = file.read()
    
    # Parse the HTML
    soup = BeautifulSoup(html_content, 'html.parser')
    
    # Find the div by ID
    target_div = soup.find('div', id=div_id)
    
    if target_div:
        # Clear existing content and add new content
        target_div.clear()
        target_div.append(BeautifulSoup(new_content, 'html.parser'))
        
        # Save the modified HTML
        output_path = output_file if output_file else html_file
        with open(output_path, 'w', encoding='utf-8') as file:
            file.write(str(soup))
        return True
    else:
        print(f"Div with ID '{div_id}' not found in the HTML file.")
        return False