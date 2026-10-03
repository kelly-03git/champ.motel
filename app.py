

    return """
<!DOCTYPE html>
<html>
<head>

    <title>Champ Motel</title>

    <meta name="description"
          content="Welcome to Champ Motel">

    <style>

        body {
            margin: 0;
            font-family: Arial, sans-serif;
            background: #f2f2f2;
            text-align: center;
        }

        header {
            background: #222;
            color: white;
            padding: 30px;
        }

        header h1 {
            font-size: 40px;
        }

        nav {
            background: #444;
            padding: 15px;
        }

        nav a {
            color: white;
            text-decoration: none;
            margin: 15px;
        }

        .hero {
            background: white;
            padding: 70px 20px;
        }

        .hero h2 {
            font-size: 40px;
        }

        .button {
            display: inline-block;
            background: #222;
            color: white;
            padding: 12px 25px;
            text-decoration: none;
            border-radius: 5px;
        }

        .rooms {
            padding: 40px 20px;
        }

        .room {
            background: white;
            width: 280px;
            margin: 20px auto;
            padding: 25px;
            border-radius: 10px;
        }

        .about {
            background: #ddd;
            padding: 40px 20px;
        }

        .contact {
            background: white;
            padding: 40px 20px;
        }

        footer {
            background: #222;
            color: white;
            padding: 20px;
        }

    </style>

</head>

<body>

    <header>

        <h1>Champ Motel</h1>

        <p>Comfort • Peace • Hospitality</p>

    </header>


    <nav>

        <a href="/">Home</a>

        <a href="#rooms">Rooms</a>

        <a href="#about">About</a>

        <a href="#contact">Contact</a>

    </nav>


    <section class="hero">

        <h2>Welcome to Champ Motel</h2>

        <p>
            Enjoy a comfortable and peaceful stay
            at Champ Motel.
        </p>

        <a href="#rooms" class="button">
            Explore Rooms
        </a>

    </section>


    <section class="rooms" id="rooms">

        <h2>Our Rooms</h2>

        <div class="room">

            <h3>Single Room</h3>

            <p>Comfortable room for one guest.</p>

            <b>₹1000 / Night</b>

        </div>


        <div class="room">

            <h3>Double Room</h3>

            <p>Comfortable room for two guests.</p>

            <b>₹1800 / Night</b>

        </div>


        <div class="room">

            <h3>Family Room</h3>

            <p>Spacious room for families.</p>

            <b>₹2500 / Night</b>

        </div>

    </section>


    <section class="about" id="about">

        <h2>About Champ Motel</h2>

        <p>
            Champ Motel is a comfortable place
            to stay and relax.
        </p>

    </section>


    <section class="contact" id="contact">

        <h2>Contact Us</h2>

        <p>Phone: +91 98765 43210</p>

        <p>Email: info@champmotel.com</p>

    </section>


    <footer>

        <p>© 2026 Champ Motel</p>

    </footer>

</body>
</html>
"""


@app.route("/api/status")
def status():

    return jsonify({
        "message": "Champ Motel Backend is running!",
        "status": "success"
    })


if _name_ == "_main_":

    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )
