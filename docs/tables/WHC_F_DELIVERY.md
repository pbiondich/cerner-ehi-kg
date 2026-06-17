# WHC_F_DELIVERY

> WHC Reporting - Fact Table containing data related to the DELIVERY

**Description:** WHC_F_DELIVERY  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 48

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMNIOINFUSION_IND` | DOUBLE |  |  | Indicator dervied from the clinical result recorded against CKI CERNER!009994F5-3734-4358-96AC-89DD83D6744E for the associated delivery. 1 = Amnioinfusion procedure occurred (any result recorded), 0 = No amnioinfusion occurred (no result recorded). |
| 2 | `ANESTHESIA_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_ANESTHESIA_GROUP.ANESTHESIA_GROUP_ID, representing a combination of anesthesia types used during the delivery in context. |
| 3 | `ATTENDING_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | foreign key to whc_d_personnel.whc_d_personnel_id corresponding to the clinical result recorded against cki CERNER!B5FCA4F5-DCAC-4CF8-A3E2-941C08D8B725 for the associated delivery. |
| 4 | `CMPLT_CERV_DIALTN_DATE_NBR` | DOUBLE | NOT NULL | FK→ | foreign key to omf_date corresponding to the clinical result recorded against cki CERNER!91F29C38-3415-4390-9FC4-95243AC9FF88 for the associated delivery. this cki corresponds to the date/time of complete cervical dilation. |
| 5 | `CMPLT_CERV_DIALTN_TIME_NBR` | DOUBLE | NOT NULL | FK→ | foreign key to omf_time corresponding to the clinical result recorded against cki CERNER!91F29C38-3415-4390-9FC4-95243AC9FF88 for the associated delivery. this cki corresponds to the date/time of complete cervical dilation. |
| 6 | `EBL_ANTEPARTUM_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!B4BFD921-2555-467C-A4F5-D4BDE2A1D20D for the associated delivery, representing Estimated Blood Loss during antepartum. |
| 7 | `EBL_ANTEPARTUM_NBR_UOM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for EBL_ANTEPARTUM_NBR. |
| 8 | `EBL_DELIVERY_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!B86970CF-9387-4327-AD17-D301CC23C9C5 for the associated delivery, representing Estimated Blood Loss during delivery. |
| 9 | `EBL_DELIVERY_NBR_UOM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for EBL_DELIVERY_NBR. |
| 10 | `EBL_POSTPART_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!16B8456F-DF6B-42BC-A6F4-D3D89DFD9C7A for the associated delivery, representing Estimated Blood Loss during postpartum. |
| 11 | `EBL_POSTPART_NBR_UOM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for EBL_POSTPARTUM_NBR. |
| 12 | `EPIDURAL_BOLUS_ANES_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded aginst CKI CERNER!818F94B7-6C9A-43D2-80AD-4C3C66D14803 for the associated delivery. This CKI corresponds to the documented date/time of the anesthesia bolus event for the epidural. |
| 13 | `EPIDURAL_BOLUS_ANES_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded aginst CKI CERNER!818F94B7-6C9A-43D2-80AD-4C3C66D14803 for the associated delivery. This CKI corresponds to the documented date/time of the anesthesia bolus event for the epidural. |
| 14 | `EPIDURAL_BOLUS_PATNT_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!CB1C7F4D-EB51-4B99-B43E-25052ED8A80E for the associated delivery. This CKI corresponds to the documented date/time of administration of the epidural bolus. |
| 15 | `EPIDURAL_BOLUS_PATNT_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!CB1C7F4D-EB51-4B99-B43E-25052ED8A80E for the associated delivery. This CKI corresponds to the documented date/time of administration of the epidural bolus. |
| 16 | `EPIDURAL_DISCONTINUED_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!49D27EC1-2C38-4B02-99D5-E474F7088BF9 for the associated delivery. This CKI corresponds to the epidural discontinue event. |
| 17 | `EPIDURAL_DISCONTINUED_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!49D27EC1-2C38-4B02-99D5-E474F7088BF9 for the associated delivery. This CKI corresponds to the epidural discontinue event. |
| 18 | `EPIDURAL_START_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!CE9BF345-3B69-4EDD-A2EB-055F0015D322 for the associated delivery. This CKI corresponds to the start date/time of the epidural. |
| 19 | `EPIDURAL_START_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!CE9BF345-3B69-4EDD-A2EB-055F0015D322 for the associated delivery. This CKI corresponds to the start date/time of the epidural. |
| 20 | `EPIDURAL_TEST_DOSE_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!54E47121-0833-440C-A1C3-B70EB9F2EBE3 for the associated delivery. This CKI correspods to the date/time the test dose was administered. |
| 21 | `EPIDURAL_TEST_DOSE_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!54E47121-0833-440C-A1C3-B70EB9F2EBE3 for the associated delivery. This CKI correspods to the date/time the test dose was administered. |
| 22 | `EPISIOTOMY_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_EPISIOTOMY.WHC_D_EPISIOTOMTY_ID, representing information related to an episiotomy associated to this delivery (if one occurred). |
| 23 | `EPISIOTOMY_IND` | DOUBLE | NOT NULL |  | Indicator derived from the clinical result recorded against either CKI CERNER!A8A46491-3471-4255-BAB1-3A9FB88ECB78 (where the result if 'YES') or CKI CERNER!155683DF-B118-4C15-B603-B750F3A6515F (where the result if 'EPISIOTOMY'). 1 = Episiotomy ocured, 0 = Episiotomy didn't occur. |
| 24 | `FETAL_POSITION_DESC` | VARCHAR(255) |  |  | User-readable description of 'Fetal Presentation' value, taken from the clinical result recorded against CKI CERNER!752D42BB-AD4D-42F9-BA9D-3CB2198588BB for the associated delivery. |
| 25 | `INDUCTION_REASON` | VARCHAR(255) |  |  | User-readable description of 'Indications for Induction' value, taken from the clinical result recorded against CKI CERNER!DCFA6EC4-8DB5-4EDB-B519-DC1E2BF3BBB4 for the associated delivery. |
| 26 | `LABOR_ONSET_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!148690D8-2679-435F-AEE3-D5F7E601E4E0 for the associated delivery. This CKI corresponds to the labor onset date/time. |
| 27 | `LABOR_ONSET_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!148690D8-2679-435F-AEE3-D5F7E601E4E0 for the associated delivery. This CKI corresponds to the labor onset date/time. |
| 28 | `LACERATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_LACERATION.WHC_D_LACERATION_ID, representing information related to a laceration associated to this delivery (if one occurred). |
| 29 | `MATERNAL_AGE_AT_DELIVERY` | DOUBLE |  |  | Calculation which is equivalent to the following in YEARS: (Delivery_Date/Time - PERSON.BIRTH_DT_TM (corresponding to the person row for MOTHER_ID) |
| 30 | `MATERNAL_COMPLICATION_DESC` | VARCHAR(255) |  |  | User-readable description of 'Maternal Delivery Complications' value, taken from the clinical result recorded against CKI CERNER!2D13D00F-BFD4-44DA-BFC3-73392A695B93 for the associated delivery. |
| 31 | `MATERNAL_COMPLICATION_GROUP_ID` | DOUBLE | NOT NULL | FK→ | foreign key to whc_d_complication_group.complication_group_id, representing a combination of complicaton types during the delivery in context. |
| 32 | `MILL_ENCNTR_ID` | DOUBLE | NOT NULL |  | This is a PK value from encounter.encntr_id, representing the underlying delivery encounter Millennium ID. |
| 33 | `MILL_PREGNANCY_ID` | DOUBLE | NOT NULL |  | Foreign key to PREGNANCY_INSTANCE.PREGNANCY_ID, representing the corresponding pregnancy in Millennium that the delivery in context is related to. |
| 34 | `MOTHER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSON.WHC_D_PERSON_ID for mother associated to the delivery in context. |
| 35 | `MOTHER_TRANSFER_TO_DESC` | VARCHAR(255) |  |  | User-readable description of 'Transfer To/From' value, taken from the clinical result recorded against CKI CERNER!05AADF41-79E7-4B96-A18F-5FC059CC280E for the associated mother. |
| 36 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_F_ORGANIZATION.WHC_D_ORGANIZATION_ID, for the organization responsible for the mother's care during the delivery. |
| 37 | `PERINEUM_INTACT_DESC` | VARCHAR(255) |  |  | User-readable description of 'Perineum Intact' value, taken from the clinical result recorded against CKI CERNER!D344529E-FBC5-4E8D-99E1-C6195274F252 for the associated delivery. |
| 38 | `PRESENTING_PART_DESC` | VARCHAR(255) |  |  | user-readable description of -Presenting Part- of a baby / each baby during a delivery - value, taken from the clinical result recorded against cki CERNER!5E8EA222-CDC3-4297-B9CA-06165BB8FB69. |
| 39 | `PRETERM_SS_DESC` | VARCHAR(255) |  |  | User-readable description of 'Preterm Labor Signs/Symptoms' value, taken from the clinical result recorded against CKI CERNER!C8C52A77-D16A-465C-8247-C79AC31A82E3 for the associated delivery. |
| 40 | `STAGE_1_OF_LABOR_IN_MIN` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoPjCqIGfQ for the associated delivery, representing the length of labor, 1st Stage in minutes. |
| 41 | `TOTAL_PRIOR_C_SECTION_NBR` | DOUBLE |  |  | sum of all previous cesarean sections for the mother in context; for millennium pregnancies, calculated by counting clinical results recorded against cerner!0b07155e-2e5c-461f-ade6-cb5768257107 (for the mother in context), where the actual result pertains to cesarean section; for historical pregnancies, calculated by counting all values of delivery method where the value represents caesarean sections |
| 42 | `TRANSACTION_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_TRANSACTION_PROFILE.WHC_D_TRANSACTION_PROFILE_ID. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `WHC_F_DELIVERY_ID` | DOUBLE | NOT NULL |  | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANESTHESIA_GROUP_ID` | [WHC_D_ANESTHESIA_GROUP](WHC_D_ANESTHESIA_GROUP.md) | `WHC_D_ANESTHESIA_GROUP_ID` |
| `ATTENDING_PHYSICIAN_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `CMPLT_CERV_DIALTN_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `CMPLT_CERV_DIALTN_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `EBL_ANTEPARTUM_NBR_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `EBL_DELIVERY_NBR_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `EBL_POSTPART_NBR_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `EPIDURAL_BOLUS_ANES_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `EPIDURAL_BOLUS_ANES_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `EPIDURAL_BOLUS_PATNT_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `EPIDURAL_BOLUS_PATNT_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `EPIDURAL_DISCONTINUED_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `EPIDURAL_DISCONTINUED_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `EPIDURAL_START_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `EPIDURAL_START_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `EPIDURAL_TEST_DOSE_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `EPIDURAL_TEST_DOSE_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `EPISIOTOMY_ID` | [WHC_D_EPISIOTOMY](WHC_D_EPISIOTOMY.md) | `WHC_D_EPISIOTOMY_ID` |
| `LABOR_ONSET_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `LABOR_ONSET_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `LACERATION_ID` | [WHC_D_LACERATION](WHC_D_LACERATION.md) | `WHC_D_LACERATION_ID` |
| `MATERNAL_COMPLICATION_GROUP_ID` | [WHC_D_COMPLICATION_GROUP](WHC_D_COMPLICATION_GROUP.md) | `WHC_D_COMPLICATION_GROUP_ID` |
| `MOTHER_ID` | [WHC_D_PERSON](WHC_D_PERSON.md) | `WHC_D_PERSON_ID` |
| `ORGANIZATION_ID` | [WHC_D_ORGANIZATION](WHC_D_ORGANIZATION.md) | `WHC_D_ORGANIZATION_ID` |
| `TRANSACTION_PROFILE_ID` | [WHC_D_TRANSACTION_PROFILE](WHC_D_TRANSACTION_PROFILE.md) | `WHC_D_TRANSACTION_PROFILE_ID` |

