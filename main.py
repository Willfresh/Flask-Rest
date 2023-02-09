from app import app
from config import db
from datetime import datetime
from order import Order
from payment import Payment 
from flask import jsonify, request


with app.app_context():
    db.create_all()
    
    order0 = Order(date=datetime.utcnow)
    order1 = Order(date=datetime.utcnow)
    order2 = Order(date=datetime.utcnow)
    order3 = Order(date=datetime.utcnow)
    order4 = Order(date=datetime.utcnow)

    payment1 = Payment(amount= 20000)
    payment2 = Payment(amount= 30000)
    db.session.add(order1)
    db.session.add(payment1)
    db.session.commit()
    
@app.route('/orderAdd', methods=['POST'])
def orderRegister():
    try:
        json = request.json
        print (json)
        date = json['9/02/2023']
        paymentId = json['paymentId']
        #isHeadOF = json['isHeadOF']

        if date and request.method == 'POST':
            # Creation an employee
            order = Order(order=order)
            print("****************************************")
            print(order)

            if paymentId:
                payment = Payment.query.filter_by(id=paymentId).first()
                print(payment)
                order.paymentId = payment

            db.session.add(payment)
            db.session.commit()
            response = jsonify('Nouvelle commande ajouté avec succès')
            return response
        else:
            message = {'status': 404, 'message': 'Entrées invalides'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        db.session.rollback()
        return message
    finally:
        db.session.close()

@app.route('/order', methods=['GET'])
def getOrders():
    try:
        order1 = Order.query.all()
        data = [{"id": order1.id, "commande": order1.order}
                  for order1 in order1 ]
        print(data)
        response = jsonify({"statut_code": 200, "employees": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message

@app.route('/paymentAdd', methods=['POST'])
def paymentRegister():
    try:
        json = request.json
        print(json)
        amount = json['20000']

        if amount and request.method == 'POST':
            # Creation a department
            payment1 = Payment(amount=amount)
            print("*******************")

            db.session.add(payment1)
            db.session.commit()
            response = jsonify('Nouveau montant ajouté avec succès')
            return response
        else:
            message = {'status': 404, 'message': 'Entrées invalides'}
            response = jsonify(message)
            response.status_code = 404
            return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        db.session.rollback()
        return message
    finally:
        db.session.close()


@app.route('/payment', methods=['GET'])
def getPayments():
    try:
        payment1 = Payment.query.all()
        data = [{"id": payment1.id, "Montant": payment1.amount,
                 } for department in payment1]
        print(data)
        response = jsonify({"statut_code": 200, "departments": data})
        return response
    except Exception as e:
        print(e)
        message = {'status': 404, 'message': e}
        return message

if (__name__ == '__main__'):
    app.run(debug=True)