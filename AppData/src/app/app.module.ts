import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';

import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { NavbarComponent } from './navbar/navbar.component';
import { AnalysisComponent } from './analysis/analysis.component';
import { Route, RouterModule } from '@angular/router';
import { HttpClientModule } from '@angular/common/http';
import { FileuploadComponent } from './fileupload/fileupload.component';
import { FormsModule, ReactiveFormsModule } from '@angular/forms';
import { Bargraph2Component } from './bargraph2/bargraph2.component';
import { Bargraph3Component } from './bargraph3/bargraph3.component';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './services/register/register.component';
import { HomeComponent } from './home/home.component';


var myRoutes:Route[]=[
  {path:'analysis',component:AnalysisComponent},
{path:'fileupload',component:FileuploadComponent},
{path:'bargraph2',component:Bargraph2Component},
{path:'bargraph3',component:Bargraph3Component},
{path:'login',component:LoginComponent},
{path:'register',component:RegisterComponent},
{path:'homepage',component:HomeComponent}]


@NgModule({
  declarations: [
    AppComponent,
    NavbarComponent,
    AnalysisComponent,
    FileuploadComponent,
    Bargraph2Component,
    Bargraph3Component,
    LoginComponent,
    RegisterComponent,
    HomeComponent
    
   
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    RouterModule.forRoot(myRoutes),
    HttpClientModule,
    FormsModule,
    ReactiveFormsModule
    
    
  
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
