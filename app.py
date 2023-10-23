from flask import Flask, render_template, request, url_for, jsonify, flash, redirect
import pygal
from pygal.style import DarkStyle
import math
import os
from flask_mail import Mail, Message
from config import BaseConfig

# from flask_sqlalchemy import SQLAlchemy

app = Flask("__name__", static_url_path="/public")

app.config.from_object(BaseConfig)
# db = SQLAlchemy(app)

from models import *

# Initiate Mail
mail = Mail(app)


@app.route("/", methods=["GET", "POST"])
def start():
    return render_template("start.html")


@app.route("/blog", methods=["GET", "POST"])
def blog():
    return render_template("blog.html")


@app.route("/calculator", methods=["GET", "POST"])
def calculator():
    return render_template("calcFAQ.html")


@app.route("/calc1", methods=["GET", "POST"])
def calc1():
    if request.method == "POST":
        w1 = float(request.form["w1"])
        w2 = float(request.form["w2"])
        w3 = float(request.form["w3"])
        w4 = float(request.form["w4"])
        w5 = float(request.form["w5"])
        w6 = float(request.form["w6"])
        w7 = float(request.form["w7"])
        w8 = float(request.form["w8"])
        w9 = float(request.form["w9"])
        w10 = float(request.form["w10"])
        h1 = float(request.form["h1"])
        h2 = float(request.form["h2"])
        h3 = float(request.form["h3"])
        h4 = float(request.form["h4"])
        h5 = float(request.form["h5"])
        h6 = float(request.form["h6"])
        h7 = float(request.form["h7"])
        h8 = float(request.form["h8"])
        h9 = float(request.form["h9"])
        h10 = float(request.form["h10"])
        wh1 = w1 * h1
        wh2 = w2 * h2
        wh3 = w3 * h3
        wh4 = w4 * h4
        wh5 = w5 * h5
        wh6 = w6 * h6
        wh7 = w7 * h7
        wh8 = w8 * h8
        wh9 = w9 * h9
        wh10 = w10 * h10
        whtotal = wh1 + wh2 + wh3 + wh4 + wh5 + wh6 + wh7 + wh8 + wh9 + wh10
        return render_template(
            "calc1.html",
            wh_1=wh1,
            wh_2=wh2,
            wh_3=wh3,
            wh_4=wh4,
            wh_5=wh5,
            wh_6=wh6,
            wh_7=wh7,
            wh_8=wh8,
            wh_9=wh9,
            wh_10=wh10,
            wh_total=whtotal,
        )
    else:
        return render_template("calc1.html")


@app.route("/calc2", methods=["GET", "POST"])
def calc2():
    if request.method == "POST":
        print(request.form)
        daily_wh = float(request.form["daily_wh"])
        batt_eff = float(request.form["batt_eff"])
        dod = float(request.form["dod"])
        temp_eff = float(request.form["temp_eff"])
        backup_days = float(request.form["backup_days"])
        voltage = float(request.form["voltage"])
        r_0 = daily_wh
        r_1 = round((daily_wh / (batt_eff / 100)), 2)
        r_2 = round((r_1 / (dod / 100)), 2)
        r_3 = round((r_2 / (temp_eff / 100)), 2)
        r_4 = round((r_3 * backup_days), 2)
        r_5 = round((r_4 / voltage), 2)
        ah_result = r_5
        return render_template(
            "calc2.html",
            r_0=r_0,
            r_1=r_1,
            r_2=r_2,
            r_3=r_3,
            r_4=r_4,
            r_5=r_5,
            ah_result=ah_result,
        )
    else:
        return render_template("calc2.html")


@app.route("/calc3", methods=["GET", "POST"])
def calc3():
    if request.method == "POST":
        select_1 = request.form.get("city_choice_1")
        select_2 = request.form.get("city_choice_2")
        # Norway
        svg = [
            13.5,
            36.4,
            83.6,
            148.6,
            199.4,
            217.3,
            184.8,
            147.1,
            96.1,
            50.0,
            19.4,
            7.8,
        ]  # Stavanger
        krs = [
            14.6,
            37.6,
            93.7,
            165.4,
            220.4,
            252.4,
            227.4,
            176.6,
            108.5,
            51.2,
            21.3,
            10.5,
        ]  # kristiansand
        osl = [
            10.4,
            33.8,
            87.4,
            148.6,
            194.2,
            218.9,
            201.5,
            154.6,
            103.0,
            49.6,
            16.4,
            6.9,
        ]  # Oslo
        trh = [
            4.5,
            23.4,
            68.9,
            124.2,
            172.6,
            183.6,
            179.4,
            143.2,
            90.6,
            39.6,
            9.7,
            1.4,
        ]  # Trondheim
        bgo = [
            9.5,
            29.8,
            70.8,
            129.7,
            183.8,
            194.8,
            170.3,
            131.6,
            84.8,
            43.5,
            14.5,
            4.5,
        ]  # Bergen
        gjo = [
            8.4,
            34.2,
            85.8,
            148.2,
            194.4,
            223.6,
            200.2,
            156.8,
            105.4,
            47.9,
            13.9,
            4.9,
        ]  # Gjovik
        kon = [
            10.1,
            33.6,
            87.9,
            147.9,
            192.6,
            217.1,
            197.3,
            151.9,
            102.1,
            47.7,
            15.0,
            5.8,
        ]  # Kongsvinger
        bei = [
            7.8,
            33.6,
            86.8,
            147.2,
            186.6,
            213.7,
            193.1,
            150.2,
            98.8,
            46.4,
            14.2,
            4.0,
        ]  # Beitostolen
        rju = [
            7.5,
            31.3,
            87.2,
            148.9,
            185.3,
            213.2,
            189.2,
            147.7,
            97.6,
            47.4,
            14.7,
            4.8,
        ]  # Rjukan
        kri = [
            4.9,
            22.7,
            65.4,
            122.2,
            175.4,
            180.7,
            171.7,
            139.0,
            82.9,
            37.8,
            10.1,
            1.9,
        ]  # kristiansund
        ale = [
            5.3,
            23.9,
            62.4,
            120.5,
            169.5,
            176.2,
            162.8,
            129.1,
            79.6,
            36.2,
            10.5,
            2.2,
        ]  # Alesund
        hau = [
            12.6,
            34.4,
            80.6,
            149.3,
            205.1,
            226.1,
            192.2,
            147.3,
            94.9,
            46.8,
            17.7,
            7.0,
        ]  # Haugesund
        lil = [
            8.1,
            33.2,
            86.3,
            147.1,
            187.3,
            217.2,
            193.4,
            151.4,
            100.8,
            46.9,
            13.9,
            4.9,
        ]  # Lillehammer
        # Sweden
        sth = [
            12.2,
            36.6,
            93.6,
            161.9,
            215.4,
            233.3,
            222.3,
            173.3,
            113.1,
            52.9,
            17.3,
            8.3,
        ]  # Stockholm
        mal = [
            19.2,
            43.0,
            103.0,
            179.2,
            229.7,
            246.7,
            232.5,
            189.3,
            132.2,
            64.7,
            26.0,
            14.4,
        ]  # Malmö
        ost = [
            4.1,
            26.3,
            80.3,
            138.3,
            188.5,
            214.3,
            200.5,
            153.7,
            92.0,
            39.3,
            9.6,
            1.6,
        ]  # Ostersund
        ore = [
            11.7,
            34.6,
            91.4,
            161.0,
            206.0,
            233.6,
            218.3,
            167.5,
            111.2,
            51.6,
            17.0,
            7.4,
        ]  # Orebro
        idr = [
            7.0,
            29.5,
            82.1,
            141.4,
            179.0,
            201.9,
            186.2,
            145.0,
            95.8,
            43.6,
            11.7,
            3.3,
        ]  # Idre
        bor = [
            9.1,
            32.5,
            90.2,
            152.0,
            195.3,
            222.9,
            207.3,
            160.3,
            103.6,
            48.8,
            14.2,
            5.8,
        ]  # Borlange
        gav = [
            10.3,
            32.7,
            91.2,
            154.5,
            205.2,
            221.2,
            214.9,
            165.5,
            105.4,
            49.0,
            14.2,
            5.6,
        ]  # Gavle
        orn = [
            4.1,
            25.8,
            79.8,
            141.4,
            206.8,
            233.4,
            218.3,
            163.2,
            95.5,
            41.5,
            9.1,
            1.8,
        ]  # Ornskoldsvik
        got = [
            15.5,
            38.8,
            94.5,
            163.6,
            211.0,
            226.3,
            212.1,
            163.0,
            110.2,
            53.9,
            20.4,
            10.6,
        ]  # Goteborg
        # Other
        par = [
            41.1,
            69.6,
            127.7,
            189.8,
            211.0,
            235.1,
            232.0,
            205.2,
            155.4,
            92.0,
            48.0,
            36.8,
        ]  # Paris
        mad = [
            94.0,
            131.8,
            186.9,
            242.6,
            282.8,
            319.5,
            334.1,
            295.7,
            229.7,
            159.2,
            105.9,
            87.2,
        ]  # Madrid
        sah = [
            186.5,
            225.9,
            271.7,
            311.2,
            327.8,
            342.9,
            335.5,
            312.1,
            268.0,
            225.6,
            191.7,
            170.9,
        ]  # Sahara
        cop = [
            19.6,
            42.0,
            98.1,
            167.8,
            216.2,
            229.8,
            216.4,
            176.7,
            122.2,
            60.2,
            24.6,
            14.4,
        ]  # Copenhagen
        ber = [
            29.0,
            57.8,
            108.6,
            176.2,
            210.3,
            233.3,
            221.2,
            192.0,
            137.8,
            74.2,
            36.7,
            23.8,
        ]  # Berlin
        mun = [
            43.4,
            74.5,
            127.5,
            178.7,
            203.5,
            219.8,
            228.7,
            208.4,
            143.8,
            92.0,
            55.0,
            40.2,
        ]  # Munich
        rom = [
            78.8,
            118.1,
            166.7,
            222.9,
            267.9,
            301.8,
            313.5,
            280.6,
            202.0,
            140.0,
            91.0,
            73.7,
        ]  # Rome
        cap = [
            354.0,
            317.2,
            254.9,
            188.6,
            124.8,
            102.4,
            116.5,
            146.1,
            197.7,
            268.7,
            319.2,
            355.9,
        ]  # Cape town

        irr_data = {
            "stavanger": svg,
            "kristiansand": krs,
            "oslo": osl,
            "stockholm": sth,
            "paris": par,
            "madrid": mad,
            "trondheim": trh,
            "bergen": bgo,
            "gjovik": gjo,
            "kongsvinger": kon,
            "beitostolen": bei,
            "rjukan": rju,
            "kristiansund": kri,
            "alesund": ale,
            "haugesund": hau,
            "lillehammer": lil,
            "malmo": mal,
            "ostersund": ost,
            "orebro": ore,
            "idre": idr,
            "borlange": bor,
            "gavle": gav,
            "ornskoldsvik": orn,
            "goteborg": got,
            "sahara": sah,
            "copenhagen": cop,
            "berlin": ber,
            "munich": mun,
            "rome": rom,
            "capetown": cap,
        }

        graph_data_1 = irr_data.get(select_1)
        graph_data_2 = irr_data.get(select_2)
        line_chart = pygal.Bar(height=450)
        line_chart.title = "Monthly average irradiation (SIS), [Wm^(-2)]"
        line_chart.x_labels = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        line_chart.add(select_1, graph_data_1)
        line_chart.add(select_2, graph_data_2)
        graph_data = line_chart.render_data_uri()
        return render_template("calc3.html", graph_data=graph_data)

    else:
        line_chart = pygal.Bar(height=450)
        line_chart.title = "Monthly average irradiation (SIS), [Wm^(-2)]"
        line_chart.x_labels = [
            "Jan",
            "Feb",
            "Mar",
            "Apr",
            "May",
            "Jun",
            "Jul",
            "Aug",
            "Sep",
            "Oct",
            "Nov",
            "Dec",
        ]
        line_chart.add("City A", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        line_chart.add("City B", [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
        graph_data = line_chart.render_data_uri()
        return render_template("calc3.html", graph_data=graph_data)


@app.route("/calc4", methods=["GET", "POST"])
def calc4():
    if request.method == "POST":
        latitude = float(request.form["latitude"])
        i_sis = float(request.form["i_sis"])
        e_d = float(request.form["e_d"])
        mpp_e = float(request.form["mpp_e"])
        if latitude > 0:
            theta = latitude + 14.6
        elif latitude < 0:
            theta = latitude - 14.6
        array_area = (e_d * math.cos(theta)) / (
            24 * math.cos(5) * i_sis * (mpp_e / 100)
        )
        array_area = abs(round(array_area, 2))
        return render_template("calc4.html", array_area=array_area)
    else:
        return render_template("calc4.html")


@app.route("/contact", methods=["GET", "POST"])
def contact_page():
    form = ContactForm()
    if request.method == "POST":
        email = request.form["email"]
        # Send to user email to administrator
        message = Message(
            request.form["subject"],
            sender=(request.form["name"], BaseConfig.EMAIL_ADDRESS),
            recipients=[BaseConfig.EMAIL_ADDRESS],
        )
        message.body = str(
            "Message using techoffgrid.com contact form\n\n"
            + email
            + "\n\n"
            + request.form["message"]
        )
        mail.send(message)

        # Send confirmation email
        msg = Message(
            "Message has been sent",
            sender=("TechOffgrid Contact Form", BaseConfig.EMAIL_ADDRESS),
            recipients=[email],
        )
        msg.body = (
            "This is an automatic email to confirm that your message has been sent from TechOffgrid.com "
            "\n\nA human will answer soon.\n\n\nThanks for reaching out."
        )
        mail.send(msg)

        flash("Your message has been sent.", "success")
        return render_template("start.html", form=form)
    else:
        return render_template("contact.html", form=form)


@app.route("/subscribe", methods=["GET", "POST"])
def subscription_page():
    form = SubscribeForm()
    if request.method == "POST":
        email = request.form["email"]
        # Send to user email to administrator
        message = Message(
            sender=(request.form["name"], BaseConfig.EMAIL_ADDRESS),
            recipients=[BaseConfig.EMAIL_ADDRESS],
        )
        message.body = str(
            "Another new subscriber at TechOffgrid.com\n\n"
            + email
            + "\n\n"
            + request.form["name"]
        )
        mail.send(message)

        # Send confirmation email
        msg = Message(
            "Subscription Confirmation",
            sender=("TechOffgrid Subscription Form", BaseConfig.EMAIL_ADDRESS),
            recipients=[email],
        )
        msg.body = (
            "This is an automatic email to confirm that you have subscribed at TechOffgrid.com "
            "\n\nWe promise not to sell your email info, and will never ever send spam.\n\nThanks"
        )
        mail.send(msg)

        flash("Subscription Registered", "success")
        return render_template("start.html", form=form)
    else:
        return render_template("subscribe.html", form=form)


if __name__ == "__main__":
    # production mode
    app.run()

    # debug mode
    # app.run(debug=True, host='0.0.0.0', port=81, use_reloader=True)
