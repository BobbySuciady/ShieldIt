<p align="center">
  <img src="https://github.com/BobbySuciady/ShieldIt/blob/main/logo.jpg" alt="ShieldKit Logo">
</p>

# ShieldKit: Your Ultimate Disaster Preparedness Companion App 🛡️

ShieldKit is your family's guardian angel in times of crisis, offering comprehensive disaster preparedness solutions.

## Our Mission 🌟

At ShieldKit, our mission is to empower families living in disaster-prone areas, especially those with vulnerable members like children, elders, or individuals with disabilities. We strive to alleviate the stress associated with disaster preparedness by providing comprehensive tools and resources, ensuring your peace of mind amidst uncertainty.

## Why We Do It ❓

Disasters and emergencies can strike unexpectedly, leaving families vulnerable and unprepared. We believe that every family deserves to feel secure and equipped to handle such situations. ShieldKit empowers you to take charge of your family's safety by facilitating the creation of personalized survival kits tailored to each member's unique needs.

## What We Offer 🛠️

- **Organize with Ease**: Effortlessly create customized survival kits for each household member, taking into account their specific requirements, such as children, elders, or disabilities.

- **Peace of Mind**: Keep track of expiration dates and receive timely reminders to ensure your survival kit remains up-to-date and ready for action.

- **Family Focused**: Simplify organization and communication by registering family members, catering to those who may be less tech-savvy.

- **Adaptable**: Customize and add new item categories based on each family member's evolving needs, ensuring comprehensive preparedness.

- **Stay Alert**: Receive timely warnings and reminders regarding item conditions and approaching disasters, keeping you informed and prepared.

- **Smart Recommendations**: Access personalized checklists and suggestions when adding new members to your family profile, ensuring nothing is overlooked.

## How To Run the App 🚀

Setting up ShieldIt on your local machine is a breeze! Follow these steps:

1. **Clone the Repository**: Execute the following command in your terminal:
    ```bash
    git clone https://github.com/BobbySuciady/ShieldIt.git
    ```

2. **Install Dependencies**: Ensure you have the latest versions of pip and brew installed. If not, run the following commands:
    ```bash
    curl https://bootstrap.pypa.io/get-pip.py -o get-pip.py
    python get-pip.py
    ```
    ```bash
    /bin/bash -c "$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/master/install.sh)"
    ```

3. **Install Required Tools**: Install the necessary tools by running the following command:
    ```bash
    pip install -r requirements.txt
    ```

4. **Start Redis and the Project**: Initiate Redis and launch the project using the following commands:
    ```bash
    brew services start redis
    honcho start
    ```

5. **View the Project**: Finally, open the following link in your preferred web browser:
    ```
    http://127.0.0.1:8000/
    ```

Now, you're all set to explore and interact with the ShieldIt project right on your local machine!

## What's Next 🚀

We're committed to continually enhancing ShieldKit to better serve you! Our upcoming development plans include:

- **Educational Resources**: Access insightful articles and tutorials on disaster preparedness, equipping you with valuable knowledge.
  
- **Marketplace Integration**: Seamlessly purchase recommended or missing items directly within the app, ensuring your survival kit is always complete.
  
- **Evacuation Planning**: Create personalized evacuation plans for your family, ensuring a smooth and organized evacuation process.
  
- **Interactive Maps**: Visualize real-time safe zones and danger areas during emergencies, helping you make informed decisions.

## Disclaimer ⚠️

Please note that ShieldKit assumes access to a smartphone with a tech-aware individual in the household. Our initial features are based on limited user research and may evolve as we gather more data.

Join us on this journey to safeguard your family and ensure peace of mind in the face of uncertainty with ShieldKit! 🌟
