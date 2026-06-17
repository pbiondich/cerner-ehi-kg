# WHC_D_TRANSACTION_PROFILE

> WHC Reporting - Dimension Table containing transaction profile Indicators

**Description:** WHC_D_TRANSACTION_PROFILE  
**Table type:** REFERENCE  
**Primary key:** `WHC_D_TRANSACTION_PROFILE_ID`  
**Columns:** 29  
**Referenced by:** 4 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COPD_PRESENT_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki CERNER!7963B3E1-0F6C-40A0-AA21-4D57220CF9AE in associated delivery. 1 = an alpha-response of 'Cephalopelvic disproportion' is recorded against the C-section indication field. |
| 2 | `CORD_BLOOD_PH_DRAWN_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!00B16C8B-7AB3-4E46-A569-CA61275B4416 for the associated delivery. 1 = cord blood pH drawn (any result recorded), 0 = cord blood PH not drawn (no result recorded). |
| 3 | `CSECTION_ELECTIVE_IND` | DOUBLE |  |  | NOT IMPLEMENTED AT THIS TIME |
| 4 | `CSECTION_EMERGENT_IND` | DOUBLE |  |  | NOT IMPLEMENTED AT THIS TIME |
| 5 | `FETALHEARTRATE_MON_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!5F5D6B1C-C75E-48A7-A1A5-672942D2AD06 in the associated delivery. 1 = fetal heart rate was monitored (any result recorded), 0 = fetal heart rate was not monitored (no result recorded). |
| 6 | `FHR_MON_DUS_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!5f5d6b1c-c75e-48a7-a1a5-672942d2ad06 in the associated delivery. 1 = fetal heart rate was using monitoring type Doppler Ultrasound, 0 fetal heart rate was not monitored using this specific monitoring type |
| 7 | `FHR_MON_FSE_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!5f5d6b1c-c75e-48a7-a1a5-672942d2ad06 in the associated delivery. 1 = fetal heart rate was using monitoring type Fetal Scalp Electrode, 0 fetal heart rate was not monitored using this specific monitoring type |
| 8 | `FHR_MON_HHD_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!5f5d6b1c-c75e-48a7-a1a5-672942d2ad06 in the associated delivery. 1 = fetal heart rate was using monitoring type Hand-held Doppler, 0 fetal heart rate was not monitored using this specific monitoring type |
| 9 | `FHR_MON_US_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!5f5d6b1c-c75e-48a7-a1a5-672942d2ad06 in the associated delivery. 1 = fetal heart rate was using monitoring type Ultrasound, 0 fetal heart rate was not monitored using this specific monitoring type |
| 10 | `FORCEPS_USE_IND` | DOUBLE |  |  | Forceps Use indicator derived from WHC_F_DELIVERY_CHILD.FORCEPS_TYPE_DESC. If WHC_F_DELIVERY_CHILD.FORCEPS_TYPE_DESC is populated for any child delivered in associated pregnancy then this indicator is set to 1, if it is not then this indicator is set to 0. |
| 11 | `GEST_AGE_GRTR_37_IND` | DOUBLE |  |  | This indicator is populated with a 1 if, for any child delivered in associated pregnancy, the gestational age result (PREGNANCY_CHILD.GESTATION_AGE) is greater than 37 weeks. |
| 12 | `HISTORY_IND` | DOUBLE |  |  | History indicator is populated with a 1 if, for the associated pregnancy, the PREGNANCY_INSTANCE.HISTORICAL_IND is set to 1. |
| 13 | `MULTIPLE_GEST_IND` | DOUBLE |  |  | Multiple Gestation indicator is populated with a 1 if, for the associated pregnancy, there are multiple WHC_F_CHILD rows. |
| 14 | `PLACENTA_TO_PATHOLOGY_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!26AE96BE-DD2A-4EA9-83E8-85A45AF7085C in the associated delivery. 1 = placenta sent to pathology (any result recorded), 0 = not sent (no result recorded). |
| 15 | `PRENATAL_CARE_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!CE9ADF19-C172-45B2-82EF-001F40C85214 in the associated delivery. 1 = Prenatal Care (any result recorded except 'NONE'), 0 = No prenatal care (no result recorded or 'NONE' recorded). |
| 16 | `PRIMIP_IND` | DOUBLE |  |  | This field is populated with a 1 if WHC_F_MOTHER_PREGNANCY.PARA_NBR is 0 and WHC_F_MOTHER_PREGNANCY.GRAVIDA_NBR is 1 for the associated pregnancy. If the calculation results in anything else, than this field is populated with a 0. |
| 17 | `PROLONGED_LABOR_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!F088C990-B188-42DE-8CD8-36D33FBC1E1A in the associated delivery. 1 = Prolonged Labor (any result recorded except 'NO'), 0 = No prolonged labor (no result recorded or 'NO' recorded). |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UTCON_MON_EXT_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!ce2b6444-ef47-4242-974b-e3568b4eda6a in the associated delivery. 1 = uterine contraction was monitored using monitoring type External, 0 uterine contraction was not monitored using this specific monitoring type |
| 24 | `UTCON_MON_IUPC_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!ce2b6444-ef47-4242-974b-e3568b4eda6a in the associated delivery. 1 = uterine contraction was monitored using monitoring type Intrauterine Pressure Catheter Placement, 0 uterine contraction was not monitored using this specific monitoring type |
| 25 | `UTCON_MON_PALP_IND` | DOUBLE |  |  | this indicator corresponds to the clinical result recorded against cki cerner!ce2b6444-ef47-4242-974b-e3568b4eda6a in the associated delivery. 1 = uterine contraction was monitored using monitoring type Palpation, 0 uterine contraction was not monitored using this specific monitoring type |
| 26 | `UTERINECONTRACTION_MON_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!CE2B6444-EF47-4242-974B-E3568B4EDA6A in the associated delivery. 1 = uterine contraction was monitored (any result recorded), 0 = uterine contraction was not monitored (no result recorded). |
| 27 | `VACUUM_USE_IND` | DOUBLE |  |  | Vacuum Use indicator derived from WHC_F_DELIVERY.VACUUM_TYPE_DESC. If WHC_F_DELIVERY.VACUUM_TYPE_DESC is populated then this indicator is set to 1, if it is not then this indicator is set to 0. |
| 28 | `VAGINAL_BIRTH_AFTER_CS_IND` | DOUBLE |  |  | Indicator set to 1 if, for the associated millennium pregnancy, the clinical result recorded against cki cerner!0b07155e-2e5c-461f-ade6-cb5768257107(delivery type) represents vaginal birth and there exists a c-section type delivery recorded prior to contextual pregnancy. indicator is set to 0 if no vaginal birth delivery type was found for the contextual pregnancy or if no cesarean sections were ever performed.For historical pregnancy, this indicator is set to 1 if the delivery method is `VBAC¿ |
| 29 | `WHC_D_TRANSACTION_PROFILE_ID` | DOUBLE | NOT NULL | PK | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (4)

| From table | Column |
|------------|--------|
| [WHC_F_CHILD](WHC_F_CHILD.md) | `TRANSACTION_PROFILE_ID` |
| [WHC_F_DELIVERY](WHC_F_DELIVERY.md) | `TRANSACTION_PROFILE_ID` |
| [WHC_F_DELIVERY_CHILD](WHC_F_DELIVERY_CHILD.md) | `TRANSACTION_PROFILE_ID` |
| [WHC_F_MOTHER_PREGNANCY](WHC_F_MOTHER_PREGNANCY.md) | `TRANSACTION_PROFILE_ID` |

