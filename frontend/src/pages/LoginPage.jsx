import React from 'react'
import * as Yup from 'yup';
import { Form, Formik } from 'formik';
import TextFieldComponent from '../components/TextFieldComponent';
import login from '../assets/login.avif';

function LoginPage() {
    const validate = Yup.object({
        username: Yup.string().min(3, 'Username must have at least 3 characters')
            .max(20, 'Username can have 20 characters maximum')
            .required('Username is required'),
        password: Yup.string().matches(/(?=.*[a-z])/, 'One lower case required')
            .matches(/(?=.*[A-Z])/, 'One upper case required')
            .matches(/(?=.*[0-9])/, 'One number required')
            .min(5, 'Password must have at least 5 characters')
            .required('Password is required')
    });
  return (

    <div className='d-flex flex-row justify-content-center align-items-center' style={{minHeight: '80vh'}}>
        <div className='col-md-5'>
            <Formik 
                initialValues={{
                    username: '',
                    password: ''
                }}
                validationSchema={validate}
            >
            {
                formik => (
                    <div>
                        <h1 className='my-4 font-weight-bold display-4'>Login Page</h1>
                        <Form>
                            <TextFieldComponent label='Username:' name='username' type='string'/>
                            <TextFieldComponent label='Password:' name='password' type='password'/>
                            <button className='btn btn-warning mt-3 me-3'>Log in</button>
                        </Form>
                        
                    </div>
                )
            }
            </Formik>
        </div>
        <div className='col-md-5 my-auto' style={{width: '30rem', marginLeft: '50px', paddingTop: '50px'}}>
            <img className='img-fluid w-100' src={login}/>
        </div>
    </div>
  )
}

export default LoginPage