links_and_buttons =[{'question': 'Change the color of the link to red.', 'answer': 'a{\n\tcolor:red;\n}', 'image': '',"starter":"a{\n\t\n}"},{'question': 'Change the cursor to a pointer.', 'answer': 'a{\n\tcursor:pointer;\n}', 'image': '',"starter":"a{\n\t\n}"},{'question': 'Fill in the blank for the first line that styles a link that the user has previously clicked.', 'answer': 'visited', 'image': 'links_buttons_9.png',"starter":""},{'question': 'Make an empty html <a> tag without any attributes.  Include the opening and closing tag.', 'answer': '<a></a>', 'image': '',"starter":""}, {'question': 'Type the name of the attribute that contains the link address.  It is 4 letters long.', 'answer': 'href', 'image': '',"starter":""}, {'question': 'Create an anchor tag that links to example.com and has a title attribute with a value of Example.  The link text should also be Example.', 'answer': '<a href="example.com" title="Example">Example</a>', 'image': '',"starter":""}, {'question': 'Create a css rule for an anchor tag.  Leave the rule empty.', 'answer': 'a{}', 'image': '',"starter":""}, {'question': 'Create a css rule for an anchor tag that makes the foreground color blue.', 'answer': 'a{color:blue;}', 'image': '',"starter":""}, {'question': 'Create an empty css rule for an a tag that has uses the hover pseudo-class', 'answer': 'a:hover{}', 'image': '',"starter":""}, {'question': 'Fill in the blank so the anchor tag is orange when the user hovers over the link', 'answer': 'orange', 'image': 'links_buttons_8.png',"starter":""}, {'question': 'Fill in the blank to complete the first line for styling a link when it is moused over or hovered.', 'answer': 'hover', 'image': 'links_buttons_9.png',"starter":""}, {'question': 'Fill in the blank for the first line that styles a link when the user clicks it.', 'answer': 'active', 'image': 'links_buttons_9.png',"starter":""}, {'question': 'Make the link below be red by default, black when visited, green when moused over and blue when active.', 'answer': 'a:link{color:red;}\na:visited{color:black;}\na:hover{color:green;}\na:active{color:blue;}\n', 'image': '',"starter":"a:link{\n\n}\na:visited{\n\n}\na:hover{\n\n}\na:active{\n\n}\n"}]


basic_html = [
  {
    "question": "Create an unordered list with the following list items: 'Apple', 'Banana', 'Cherry'.",
    "answer": "<ul><li>Apple</li><li>Banana</li><li>Cherry</li></ul>",
    "image": "",
    "starter":"""
    <ul>
      <li>Apple</li>
      <li>Banana</li>
      <li>      </li>
    </ul>
    """
  },
  {
    "question": "Create a paragraph with the text 'This is a simple paragraph.'.",
    "answer": "<p>This is a simple paragraph.</p>",
    "image": "","starter":""
  },
  {
    "question": "Write the HTML to create an ordered list with the following items: 'First', 'Second', 'Third'.",
    "answer": "<ol><li>First</li><li>Second</li><li>Third</li></ol>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create a hyperlink that opens in a new tab and links to 'https://example.com'.",
    "answer": "<a href='https://example.com' target='_blank'>Visit Example</a>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create a heading (h1) with the text 'Welcome to My Website'.",
    "answer": "<h1>Welcome to My Website</h1>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create a line break in your page using HTML.",
    "answer": "<br>",
    "image": "",
    "starter":""
  },
  {
    "question": "Write the HTML to create a heading (h2) called 'Services'.",
    "answer": "<h2>Services</h2>",
    "image": "",
    "starter":""
  },
  {
    "question": "Create an image with the source 'https://example.com/logo.png' and the alt text 'Company Logo'.",
    "answer": "<img src='https://example.com/logo.png' alt='Company Logo'>",
    "image": "https://upload.wikimedia.org/wikipedia/commons/thumb/e/e5/HTML5_Logo.svg/1280px-HTML5_Logo.svg/1280px-HTML5_Logo.svg.png",
    "starter":""
  },
  {
    "question": "Create an unordered list with the following items: 'HTML', 'CSS', 'JavaScript'.",
    "answer": "<ul><li>HTML</li><li>CSS</li><li>JavaScript</li></ul>",
    "image": "",
    "starter":""
  },

]


python_loops = [
  {
    "question": "Complete the for-loop that prints numbers from 1 to 5.\nUse 'i' as the variable.\nUse the tab key for indentation.",
    "answer": "for i in range(1, 6):\n\tprint(i)",
    "image": "","starter":"for i in range(______):\n\t"
    
  },
  {
    "question": "Use a for-loop to print each character in the string 'Python'.\n Use 'char' as the target variable\nUse the tab key for indentation.",
    "answer": "for char in 'Python':\n\t print(char)",
    "image": "","starter":""
  },
  {
    "question": "Write a loop that prints only even numbers from 2 to 10.\nUse 'i' as the variable.\nUse the tab key for indentation.",
    "answer": "for i in range(2, 11, 2):\n\t print(i)",
    "image": "","starter":"for i in range(__,__,__):\n\t"
  },
  {
    "question": "Use a while-loop to print numbers from 10 down to 1.\nUse 'i' as the variable..\nUse the tab key for indentation.",
    "answer": "i = 10\nwhile i > 0:\n\tprint(i)\n\ti -= 1",
    "image": "","starter":"i=10\n"
  },
  {
    "question": "Write a loop that iterates through a list of numbers [3, 6, 9] and prints each number.\nThe list is saved in a variable called 'numbers'.\nUse the target variable 'num' in your for loop.\nUse the tab key for indentation.",
    "answer": "numbers = [3, 6, 9]\nfor num in numbers:\n\tprint(num)",
    "image": "","starter":"numbers = [3, 6, 9]\n"
  }
]


css_borders_padding =[
    {
        "question": "Add a solid red border of 2px around a div element.",
        "answer": "div { border: 2px solid red; }",
        "image": "",
        "starter": "div {\n    \n}"
    },
    {
        "question": "Set the padding of a paragraph to 20px on all sides.",
        "answer": "p { padding: 20px; }",
        "image": "",
        "starter": "p {\n    \n}"
    },
    {
        "question": "Create a div with a 10px margin on the top and bottom, but 5px on the sides.",
        "answer": "div { margin: 10px 5px; }",
        "image": "",
        "starter": "div {\n    \n}"
    },
    {
        "question": "Apply a dotted blue border of 3px to a span element.",
        "answer": "span { border: 3px dotted blue; }",
        "image": "",
        "starter": "span {\n    \n}"
    },
    {
        "question": "Set the left margin of a div to 50px and the right padding to 30px.",
        "answer": "div { margin-left: 50px; padding-right: 30px; }",
        "image": "",
        "starter": "div {\n    \n}"
    },
    {
        "question": "Make a div have a border-radius of 15px and a solid black border.",
        "answer": "div { border: 2px solid black; border-radius: 15px; }",
        "image": "",
        "starter": "div {\n    \n}"
    },
    {
        "question": "Set the padding-top of a paragraph to 25px.",
        "answer": "p { padding-top: 25px; }",
        "image": "",
        "starter": "p {\n    \n}"
    },
    {
        "question": "Apply a double green border of 4px to a div element.",
        "answer": "div { border: 4px double green; }",
        "image": "",
        "starter": "div {\n    \n}"
    },
    {
        "question": "Add 20px of padding only to the left side of a paragraph.",
        "answer": "p { padding-left: 20px; }",
        "image": "",
        "starter": "p {\n    \n}"
    },
    {
        "question": "Create a div with different margin values: 5px top, 10px right, 15px bottom, and 20px left.",
        "answer": "div { margin: 5px 10px 15px 20px; }",
        "image": "",
        "starter": "div {\n    \n}"
    }
]