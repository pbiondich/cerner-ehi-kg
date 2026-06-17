# WHC_F_DELIVERY_CHILD

> WHC Reporting - Fact Table containing data related to the DELIVERY and CHILD

**Description:** WHC_F_DELIVERY_CHILD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 43

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `AMNIOTIC_FLUID_COLOR_DESC` | VARCHAR(255) |  |  | Description corresponding to the clinical result recorded agaisnt CKI CERNER!2271786D-245C-448C-BD01-9D6AE23FA313 for the associated child. |
| 2 | `ANESTHESIOLOGIST_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!676B955C-EB41-4E5D-A847-08914BAD33AE for the associated child. |
| 3 | `ANESTHETIST_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!239377AD-E73F-4863-B341-D791662E4E2D for the associated child. |
| 4 | `ASST_PHYSICIAN_1_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!F585EADF-7F01-46CD-8D43-1C7B01C17592 for the associated child. |
| 5 | `ASST_PHYSICIAN_2_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!F585EADF-7F01-46CD-8D43-1C7B01C17592 for the associated child. |
| 6 | `AUGMENT_METHOD_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_AUGMENT_METHOD_GROUP.WHC_D_AUGMENT_METHOD_GROUP_ID, representing a combination of augmentation methods used during the delivery of the child in context. |
| 7 | `CHILD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSON.WHC_D_PERSON_ID for the associated child. |
| 8 | `CORD_BB_TO_LAB_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!6341CE73-C324-4B96-A633-89A3057DDB4E in the associated delivery of the child. 1 = Cord Blood sent to Lab (any result recorded except 'NO'), 0 = Cord blood not sent to Lab (no result recorded or 'NO' recorded). |
| 9 | `CSECTION_INDCN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_CSECTION_INDCN.WHC_D_CSECTION_INDCN_ID, representing information related to a casearean section associated to the child in context (if one occurred for the child on context). |
| 10 | `DELIVERY_CNM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!61327197-713E-43CE-904C-20C5C98DED1B for the associated child. |
| 11 | `DELIVERY_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoPTCqIGfQ for the associated child. |
| 12 | `DELIVERY_PEDIATRICIAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!ABEA0D57-6F36-4252-9338-C33C70C69978 for the associated child. |
| 13 | `DELIVERY_PHYSICIAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!148D82CA-6CCA-437C-818A-FC0BDE22EF2F for the associated child. |
| 14 | `DELIVERY_RN_1_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!7DC28206-7A88-4CC1-B53E-1C5C33DF9B9D for the associated child. |
| 15 | `DELIVERY_RN_2_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!7DC28206-7A88-4CC1-B53E-1C5C33DF9B9D for the associated child. |
| 16 | `DELIVERY_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoPTCqIGfQ for the associated child. |
| 17 | `DELIVERY_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_DELIVERY_TYPE.WHC_D_DELIVERY_TYPE_ID, representing the delivery type for the associated child. |
| 18 | `FORCEPS_TYPE_DESC` | VARCHAR(255) |  |  | User-readable description of 'Forceps Type' value, taken from the clinical result recorded against CKI CERNER!AAAC3B27-F5EF-4455-B40F-BF6C8A82669A for the associated child. |
| 19 | `INDUCTION_METHOD_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_INDCTN_METHOD_GROUP.WHC_D_INDCTN_METHOD_GROUP_ID, representing a combination of induction methods used during the delivery of the child in context. |
| 20 | `LABOR_ONSET_METHOD_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_LABOR_ONS_MTHD_GROUP.WHC_D_LABOR_ONS_MTHD_GROUP_ID, representing a combination of labor onset methods used during the delivery of the child in context. |
| 21 | `MILL_PREGNANCY_ID` | DOUBLE | NOT NULL |  | Foreign key to PREGNANCY_INSTANCE.PREGNANCY_ID, representing the corresponding pregnancy in Millennium. |
| 22 | `PLACENTA_DELIVERY_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!DBCD00BD-E56D-4987-BDE4-FA7D0BA9449C for the child on context. This CKI corresponds to the placenta delivery event date/time. |
| 23 | `PLACENTA_DELIVERY_METHOD_DESC` | VARCHAR(255) |  |  | User-readable description of 'Placenta Delivery Method' value, taken from the clinical result recorded against CKI CERNER!EEA339C6-8E94-4037-A702-C69A942DBADD for the child in context. |
| 24 | `PLACENTA_DELIVERY_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!DBCD00BD-E56D-4987-BDE4-FA7D0BA9449C for the child on context. This CKI corresponds to the placenta delivery event date/time. |
| 25 | `PRECIPITIOUS_LABOR_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!F37DB9C1-E43D-402C-B4A8-B90B0D943310 in the associated delivery of the child. 1 = Precipitious Labor (any result recorded except 'NO'), 0 = No precipitious labor (no result recorded or 'NO' recorded). |
| 26 | `PROLONGED_ROM_IND` | DOUBLE |  |  | This indicator corresponds to the clinical result recorded against CKI CERNER!433B91EB-1996-41A7-BE2C-01685AC84927 in the associated delivery of the child. 1 = Prolonged Rupture of Membranes (any result recorded except 'NO'), 0 = No prolonged ROM (no result recorded or 'NO' recorded). |
| 27 | `RESUS_RN_1_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!D216FB18-2E6A-4341-A200-D22811FDEC58 for the associated child. |
| 28 | `ROM_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to the clinical result recorded against CKI CERNER!17A18CD6-CA24-4AC2-B80B-27B61A62D253 for the child on context. This CKI corresponds to the ROM event date/time. |
| 29 | `ROM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_ROM.WHC_D_ROM_ID, representing the rupture of membranes for the associated child. |
| 30 | `ROM_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to the clinical result recorded against CKI CERNER!17A18CD6-CA24-4AC2-B80B-27B61A62D253 for the child on context. This CKI corresponds to the ROM event date/time. |
| 31 | `ROM_TO_DELIVERY_TIME_MINS` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!7DB3D314-2095-485D-98B9-7E14FA4A1E5F for the child on context, representing the duration between Rupture of Membranes and Delivery in minutes. |
| 32 | `SCRUB_TECHNICIAN_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSONNEL.WHC_D_PERSONNEL_ID corresponding to the clinical result recorded against CKI CERNER!263C8F20-C96A-45F8-99EB-BB7C964F8C3B for the associated child. |
| 33 | `STAGE_2_OF_LABOR_IN_MIN` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoPvCqIGfQ for the associated child, representing the length of labor, 2nd Stage in minutes. |
| 34 | `STAGE_3_OF_LABOR_IN_MIN` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoP7CqIGfQ for the associated child, representing the length of labor, 3rd Stage in minutes. |
| 35 | `TOTAL_LENGTH_LABOR_MINS` | DOUBLE |  |  | Calculation as follows: WHC_F_DELIVERY.STAGE_1_OF_LABOR_IN_MIN (from associated delivery) + WHC_F_DELIVERY_CHILD.STAGE_2_OF_LABOR_IN_MIN + WHC_F_DELIVERY_CHILD.STAGE_3_OF_LABOR_IN_MIN |
| 36 | `TRANSACTION_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_TRANSACTION_PROFILE.WHC_D_TRANSACTION_PROFILE_ID. |
| 37 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 38 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 39 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 40 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 41 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 42 | `VACUUM_TYPE_DESC` | VARCHAR(255) |  |  | User-readable description of 'Vacuum Type' value, taken from the clinical result recorded against CKI CERNER!B0CEC3B2-1F85-4877-81C4-D33EB13C07B9 for the associated child. |
| 43 | `WHC_F_DELIVERY_CHILD_ID` | DOUBLE | NOT NULL |  | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ANESTHESIOLOGIST_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `ANESTHETIST_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `ASST_PHYSICIAN_1_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `ASST_PHYSICIAN_2_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `AUGMENT_METHOD_GROUP_ID` | [WHC_D_AUGMENT_METHOD_GROUP](WHC_D_AUGMENT_METHOD_GROUP.md) | `WHC_D_AUGMENT_METHOD_GROUP_ID` |
| `CHILD_ID` | [WHC_D_PERSON](WHC_D_PERSON.md) | `WHC_D_PERSON_ID` |
| `CSECTION_INDCN_ID` | [WHC_D_CSECTION_INDCN](WHC_D_CSECTION_INDCN.md) | `WHC_D_CSECTION_INDCN_ID` |
| `DELIVERY_CNM_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `DELIVERY_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `DELIVERY_PEDIATRICIAN_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `DELIVERY_PHYSICIAN_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `DELIVERY_RN_1_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `DELIVERY_RN_2_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `DELIVERY_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `DELIVERY_TYPE_ID` | [WHC_D_DELIVERY_TYPE](WHC_D_DELIVERY_TYPE.md) | `WHC_D_DELIVERY_TYPE_ID` |
| `INDUCTION_METHOD_GROUP_ID` | [WHC_D_INDCTN_METHOD_GROUP](WHC_D_INDCTN_METHOD_GROUP.md) | `WHC_D_INDCTN_METHOD_GROUP_ID` |
| `LABOR_ONSET_METHOD_GROUP_ID` | [WHC_D_LABOR_ONS_MTHD_GROUP](WHC_D_LABOR_ONS_MTHD_GROUP.md) | `WHC_D_LABOR_ONS_MTHD_GROUP_ID` |
| `PLACENTA_DELIVERY_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `PLACENTA_DELIVERY_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `RESUS_RN_1_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `ROM_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `ROM_ID` | [WHC_D_ROM](WHC_D_ROM.md) | `WHC_D_ROM_ID` |
| `ROM_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `SCRUB_TECHNICIAN_ID` | [WHC_D_PERSONNEL](WHC_D_PERSONNEL.md) | `WHC_D_PERSONNEL_ID` |
| `TRANSACTION_PROFILE_ID` | [WHC_D_TRANSACTION_PROFILE](WHC_D_TRANSACTION_PROFILE.md) | `WHC_D_TRANSACTION_PROFILE_ID` |

