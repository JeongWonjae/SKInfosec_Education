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
    res.send('welcome to skinfosec enka home service : ' + ip + "," + new Date());
});

app.get('/health', (req, res) => {
      res.status(200).send();
});

app.get('/updateCustomer', (req, res) => {
  let type=req.param('type');
  let content=req.param('content');
  let id=req.param('id');
  connection.query('update customer set '+type+'=\''+content+'\' where customer_id=\''+id+'\'',(error,rows) => {
    if (error) throw error;
    console.log('result is :: ', rows);
    res.send(rows);
  });
});

app.get('/updateCar', (req, res) => {
  let type=req.param('type');
  let content=req.param('content');
  let id=req.param('id');
  connection.query('update car_menu set '+type+'=\''+content+'\' where car_id=\''+id+'\'',(error,rows) => {
    if (error) throw error;
    console.log('result is : ', rows);
    res.send(rows);
  });
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

app.get('/car', (req, res) => {
  let id=req.param('id')
  connection.query('select * from car_menu WHERE car_id=\''+id+'\'', (error, rows) => {
    if (error) throw error;
    console.log('Car info is: ', rows);
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

app.get('/customerdelete', (req, res) => {
  let id=req.param('id');
  connection.query('DELETE FROM customer WHERE customer_id=\'' + id + '\'', (error, rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/cardelete', (req, res) => {
  let id=req.param('id');
  connection.query('DELETE FROM car_menu WHERE car_id=\'' + id + '\'', (error, rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/serviceChoice/yes', (req, res) => {
  let id=req.param('id');
  connection.query('SELECT DISTINCT product_name FROM product WHERE service_menu_service_id=\'' + id + '\'', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});


app.get('/lookupService', (req, res) => {
  let custid=req.param('custid');
  connection.query('SELECT * FROM service_records sr LEFT JOIN (SELECT product_id, service_menu_service_id, product_name, parts_name, parts_price from product p1, product_menu pm WHERE p1.parts_id=pm.parts_id) AS p ON sr.product_id=p.product_id LEFT JOIN service_menu sm ON sr.service_id=sm.service_id WHERE sr.customer_customer_id=\''+custid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/lookupMechanic', (req, res) => {
  let serviceid=req.param('serviceid');
  connection.query('SELECT mechanic_name FROM management m, mechanic mc WHERE m.mechanic_mechanic_id=mc.mechanic_id AND m.service_record_id=\''+serviceid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/service', (req, res) => {
  connection.query('select * from service_menu', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/lookupMechanics', (req, res) => {
  connection.query('select * from mechanic', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/lookupTicket', (req, res) => {
  let custid=req.param('custid');
  connection.query('select service_ticket_id from service_records where customer_customer_id=\''+custid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});


app.get('/serviceChoice', (req, res) => {
  let id=req.param('id');
  connection.query('select need_product from service_menu where service_id=\'' + id + '\'', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});


app.get('/checkTicket', (req, res) => {
  let ticket=req.param('ticket');
  connection.query('select service_ticket_id from service_records where service_ticket_id=\''+ticket+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/addServiceRecords', (req, res) => {
  let serviceid=req.param('serviceid');
  let serviceselect=req.param('serviceselect');
  let ticket=req.param('ticket');
  let day=req.param('day');
  let custid=req.param('custid');
  connection.query('insert into service_records values(\''+serviceid+'\',\''+serviceselect+'\',NULL,\''+ticket+'\',\''+day+'\',\''+custid+'\')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/addServiceRecords_parts', (req, res) => {
  let serviceid=req.param('serviceid');
  let serviceselect=req.param('serviceselect');
  let selectparts=req.param('selectparts');
  let ticket=req.param('ticket');
  let day=req.param('day');
  let custid=req.param('custid');
  connection.query('insert into service_records values(\''+serviceid+'\',\''+serviceselect+'\',(select product_id from product where parts_id=\''+selectparts+'\'),\''+ticket+'\',\''+day+'\',\''+custid+'\')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/addManagement', (req, res) => {
  let mecaid=req.param('mecaid');
  let serviceid=req.param('serviceid');
  connection.query('insert into management values(\''+mecaid+'\',\''+serviceid+'\')',(error,rows) => {
    if (error) throw error;
    res.send('success');
  });
});

app.get('/service/getMecanic', (req, res) => {
  let serviceid=req.param('serviceid');
  connection.query('SELECT mc.mechanic_name from management ma, mechanic mc where ma.mechanic_mechanic_id=mc.mechanic_id AND service_record_id=\''+serviceid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});


app.get('/service/getName', (req, res) => {
  let serviceid=req.param('serviceid');
  connection.query('SELECT sm.service_name FROM service_menu sm, service_records sr WHERE sm.service_id=sr.service_id AND sr.service_record_id=\''+serviceid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/service/getCustName', (req, res) => {
  let serviceid=req.param('serviceid');
  connection.query('SELECT c.customer_name FROM customer c, service_records sr WHERE c.customer_id=sr.customer_customer_id AND sr.service_record_id=\''+serviceid+'\'',(error,rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/parts', (req, res) => {
  let parts_name=req.param('parts_name');
  connection.query('select * from product_menu where parts_name like\'' + parts_name + '\'', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/product', (req, res) => {
  let id=req.param('id');
  connection.query('SELECT parts_name FROM product p, product_menu pm WHERE p.parts_id=pm.parts_id and p.parts_id=\'' + id + '\'', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/mechanic', (req, res) => {
  connection.query('select * from mechanic', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.get('/mechanicChoice', (req, res) => {
  let id=req.param('id');  
  connection.query('select mechanic_name from mechanic where mechanic_id=\'' +id+ '\'', (error, rows) => {
    if (error) throw error;
    res.send(rows);
  });
});

app.listen(app.get('port'), () => {
  console.log('Express server listening on port ' + app.get('port'));
});
