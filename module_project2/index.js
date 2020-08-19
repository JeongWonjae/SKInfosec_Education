const express    = require('express');
const mysql      = require('mysql');
const dbconfig   = require('./config/database.js');
const connection = mysql.createConnection(dbconfig);

const app = express();

app.set('port', process.env.PORT || 8000);

app.get('/', (req, res) => {
    var ip = req.headers['x-forwarded-for'] ||
                req.connection.remoteAddress ||
                req.socket.remoteAddress ||
            (req.connection.socket ? req.connection.socket.remoteAddress : null);
    console.log(ip);
    res.send('Hello, World! : ' + ip + "," + new Date());
});
app.get('/health', (req, res) => {
      res.status(200).send();
});

app.get('/getId', (req, res) => {
  let table=req.param('tName');
  let attribute=req.param('tAttr');
  let length=parseInt(req.param('pLen'));
  connection.query('select lpad(max(convert(substr('+attribute+','+(length+1)+','+(length+4)+'),signed)+1),4,0) as id from '+table,(error,rows) => {
    if (error) throw error;
    console.log('result is : ', rows);
    res.send(rows);
  });
});

app.get('/addCustomer', (req, res) => {
  let cusid=req.param('custid'); 
  let name=req.param('name');
  let phone=req.param('phone');
  let addr=req.param('addr');
  connection.query('insert into customer values(\''+cusid+'\',\''+name+'\',\''+phone+'\',\''+addr+'\')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/addCar', (req, res) => {
  let carid=req.param('carid');
  let model=req.param('model');
  let color=req.param('color');
  let stat=req.param('status');
  let number=req.param('number');
  let year=req.param('year');
  let price=req.param('price');
  connection.query('insert into car_menu values(\''+carid+'\',\''+model+'\',\''+color+'\',\''+stat+'\',\''+number+'\',\''+year+'\',\''+price+'\')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/customers', (req, res) => {
  connection.query('select * from customer', (error, rows) => {
    if (error) throw error;
    console.log('Customer info is: ', rows);
    res.send(rows);
  });
});

app.get('/customer', (req, res) => {
  let id=req.param('id')
  connection.query('select * from customer WHERE customer_id=\''+id+'\'', (error, rows) => {
    if (error) throw error;
    console.log('Customer info is: ', rows);
    res.send(rows);
  });
});

app.get('/cars', (req, res) => {
  connection.query('SELECT * FROM car_menu WHERE car_id NOT IN(SELECT car_menu_car_id FROM order_details)', (error, rows) => {
    if (error) throw error;
    console.log('Car info is: ', rows);
    res.send(rows);
  });
});

app.get('/salesperson', (req, res) => {
  let id=req.param('id')
  connection.query('select * from salesperson where salesperson_id=\''+id+'\'', (error, rows) => {
    if (error) throw error;
    console.log('salesperson info is: ', rows);
    res.send(rows);
  });
});

app.get('/carprice', (req, res) => {
  let id=req.param('carid')
  connection.query('select car_price from car_menu where car_id=\''+id+'\'', (error, rows) => {
    if (error) throw error;
    console.log('car price is: ',rows);
    res.send(rows);
  });
});

app.get('/addOrder', (req, res) => {
  let orderid=req.param('orderid');
  let custid=req.param('custid');
  let car=req.param('carid');
  let carprice=parseInt(req.param('carprice'));
  connection.query('insert into order_details values(\''+orderid+'\',\''+custid+'\',\'\',\''+car+'\','+carprice+')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/addInvoice', (req, res) => {
  let invoiceid=req.param('invoiceid');
  let custid=req.param('custid');
  let salesid=req.param('salesid');
  let orderid=req.param('orderid');
  connection.query('insert into sales_invoice values(\''+invoiceid+'\',\''+custid+'\',\''+salesid+'\',\''+orderid+'\')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/lookupInvoice', (req, res) => {
  let invoiceid=req.param('invoiceid');
  connection.query('SELECT ct.customer_name, cm.car_model, cm.car_color, cm.new_old_state, cm.serial_number, cm.car_year, cm.car_price, sp.salesperson_name FROM customer ct, car_menu cm, sales_invoice si, order_details od, salesperson sp WHERE si.customer_customer_id=ct.customer_id AND si.order_details_order_id=od.order_id AND od.car_menu_car_id=cm.car_id AND sp.salesperson_id=si.salesperson_salesperson_id AND si.invoice_id=\''+invoiceid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});


app.listen(app.get('port'), () => {
  console.log('Express server listening on port ' + app.get('port'));
});
