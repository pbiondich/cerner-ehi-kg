# WHC_F_CHILD

> WHC Reporting - Fact Table containing data related to the CHILD

**Description:** WHC_F_CHILD  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 63

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABDOMINAL_CIRCUMFERENCE_NBR` | DOUBLE |  |  | Value of the clinical result recorded against CKI CERNER!1A272109-D817-4650-AA83-AC2AE218D594 for the associated child, representing Abdominal Circumference |
| 2 | `ABDOMINAL_CIRCUMFRNCE_UOM_DESC` | VARCHAR(255) |  |  | Description of the unit of measure corresponding to WHC_F_CHILD. ABDOMINAL_CIRCUMFERENCE_NBR, representing the Unit of Measurement for Abdominal Circumference |
| 3 | `ABDOMINAL_CIRCUMFRNCE_UOM_ID` | DOUBLE |  | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for abdominal_circumference_nrb. |
| 4 | `AMT_TIME_FOR_SKIN_SKIN_INI_MIN` | DOUBLE |  |  | Value corresponding to the clinical result recroded against CKI CERNER!43811D11-9A98-4E88-B14B-13AE3D359883 for the associated child, representing the 'Amount of Time for Skin to Skin Contact'. |
| 5 | `ANESTHESIA_GROUP_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_ANESTHESIA_GROUP.ANESTHESIA_GROUP_ID, representing a combination of anesthesia types used during the delivery of the child in context. |
| 6 | `APGAR_10_NBR` | DOUBLE |  |  | value corresponding to the clinical result recorded against cki cerner!9900d029-8186-45d9-b9c6-49594e976ed2 for the associated child, representing the 'apgar score 10 minute'; -1 default for unrecorded score' |
| 7 | `APGAR_15_NBR` | DOUBLE |  |  | value corresponding to the clinical result recorded against cki cerner!b48bbcd8-68fe-40a2-9438-f158cd0caf7f for the associated child, representing the 'apgar score 15 minute'; -1 default for unrecorded score |
| 8 | `APGAR_1_NBR` | DOUBLE |  |  | value corresponding to the clinical result recorded against cki cerner!b6edb709-4db0-4718-b897-e198850fea3e for the associated child, representing the 'apgar score 1 minute'; -1 default for unrecorded score |
| 9 | `APGAR_20_NBR` | DOUBLE |  |  | value corresponding to the clinical result recorded against cki cerner!98807d2c-601b-4b4c-a685-68ace052748c for the associated child, representing the 'apgar score 20 minute'; -1 default for unrecorded score' |
| 10 | `APGAR_5_NBR` | DOUBLE |  |  | value corresponding to the clinical result recorded against cki cerner!a1eedca0-dd0b-4a6b-9381-e7492d5409b1 for the associated child, representing the 'apgar score 5 minute'; -1 default for unrecorded score' |
| 11 | `BABY_LABEL` | VARCHAR(20) |  |  | User-readable description of 'Baby' value, taken from the clinical result recorded against CKI CERNER!D895A6C5-57CA-4406-904E-DC967A1CD161. |
| 12 | `BABY_MRN` | VARCHAR(50) |  |  | Value of ENCNTR_ALIAS.ALIAS (of type 'MRN') for the associated child, representing the Medical Record Number of the child. |
| 13 | `BIRTH_HEIGHT_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!28B30F66-EEAF-4016-B0F5-100ECC928477 for the associated child, representing the 'Birth Length'. |
| 14 | `BIRTH_HEIGHT_UOM_DESC` | VARCHAR(255) |  |  | Description of the unit of measure correpsonding to WHC_F_CHILD.BIRTH_HEIGHT_NBR, representing the Unit of Measurement for Birth Height. |
| 15 | `BIRTH_HEIGHT_UOM_ID` | DOUBLE |  | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for birth_height_nbr. |
| 16 | `BIRTH_ORDER` | VARCHAR(10) |  |  | NOT IMPLEMENTED AT THIS TIME |
| 17 | `BIRTH_WEIGHT_NBR` | DOUBLE |  |  | Value of PREGNANCY_CHILD.WEIGHT_AMT for the associated child representing the Birth Weight. |
| 18 | `BIRTH_WEIGHT_UOM_DESC` | VARCHAR(255) |  |  | Display value of PREGNANCY_CHILD.WEIGHT_UNIT_CD for the associated child, representing the Unit of Measurement for Birth Weight. |
| 19 | `BIRTH_WEIGHT_UOM_ID` | DOUBLE |  | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for birth_weight_nbr. |
| 20 | `CHEST_CIRCUMFERENCE_NBR` | DOUBLE |  |  | Value of the clinical result recorded against CKI CERNER!71FDF27E-BB08-4C39-85DE-76662A6A1B53 for the associated child, representing Birth Chest Circumference. |
| 21 | `CHEST_CIRCUMFERENCE_UOM_DESC` | VARCHAR(255) |  |  | Description of the unit of measure correpsonding to WHC_F_CHILD.CHEST_CIRCUMFERENCE_NBR, representing the Unit of Measurement for Chest Circumference. |
| 22 | `CHEST_CIRCUMFERENCE_UOM_ID` | DOUBLE |  | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for chest_circumference_nrb. |
| 23 | `CHILD_BIRTH_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE, corresponding to the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoPTCqIGfQ for the associated child. This CKI corresponds to the 'Date and Time of Birth' for the child. |
| 24 | `CHILD_BIRTH_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME, corresponding to the clinical result recorded against CERNER!ASYr9AEYvUr1YoPTCqIGfQ for the associated child. This CKI corresponds to the 'Date and Time of Birth' for the child. |
| 25 | `CHILD_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSON.WHC_D_PERSON_ID for the associated child. |
| 26 | `CHILD_TRANSFERED_TO_DESC` | VARCHAR(255) |  |  | User-readable description of 'Transfer To/From' value, taken from the clinical result recorded against CKI CERNER!73F036A3-D3EB-46F8-8A58-47EA59F2DE1A for the associated child. |
| 27 | `CORD_DESC` | VARCHAR(255) |  |  | User-readable description of 'Umbilical Cord Description' value, taken from the clinical result recorded against CKI CERNER!DFC618AA-2F70-4E87-A410-882393B81262 for the associated child. |
| 28 | `DELIVERY_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_DELIVERY_TYPE.WHC_D_DELIVERY_TYPE_ID, representing the delivery type for the associated child. |
| 29 | `FETAL_COMPLICATION_GROUP_ID` | DOUBLE |  | FK→ | foreign key to whc_d_complication_group.whc_d_complication_group_id, representing a combination of fetal complication types for the child in context. |
| 30 | `GESTATIONAL_AGE_BIRTH_NBR` | DOUBLE |  |  | Value of PREGNANCY_CHILD.GESTATION_AGE for the associated child. |
| 31 | `HEAD_CIRCUMFERENCE_NBR` | DOUBLE |  |  | Value corresponding to the clinical result recorded against CKI CERNER!DF1F749C-6B87-4AC8-91FF-718C41678BC7 for the associated child, representing Birth Head Circumference. |
| 32 | `HEAD_CIRCUMFERNENCE_UOM_DESC` | VARCHAR(255) |  |  | Description of the unit of measure correpsonding to WHC_F_CHILD.HEAD_CIRCUMFERENCE_NBR, representing the Unit of Measurement for Head Circumference. |
| 33 | `HEAD_CIRCUMFERNENCE_UOM_ID` | DOUBLE |  | FK→ | Foreign key to whc_d_uom_type.whc_d_uom_type_id, representing the unit of mesure used for head_circumference_nrb. |
| 34 | `LABOR_DURATION_MINS` | DOUBLE |  |  | Same value as for WHC_F_DELIVERY_CHILD.TOTAL_LENGTH_LABOR_MINS |
| 35 | `MILL_PREGNANCY_ID` | DOUBLE | NOT NULL |  | Foreign key to PREGNANCY_INSTANCE.PREGNANCY_ID, representing the corresponding pregnancy in Millennium. |
| 36 | `MOTHER_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_PERSON.WHC_D_PERSON_ID for the mother associated to the child on context. |
| 37 | `NEONATE_ADMISSION_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to ENCOUNTER.REG_DT_TM for the associated child's encounter created after delivery (between delivery date time for the associated pregnancy and the pregnancy close date time). |
| 38 | `NEONATE_ADMISSION_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to ENCOUNTER.REG_DT_TM for the associated child's encounter created after delivery (between delivery date time for the associated pregnancy and the pregnancy close date time). |
| 39 | `NEONATE_COMPLICATION_DESC` | VARCHAR(255) |  |  | User-readable description of 'Neonate Complications' value, taken from the clinical result recorded against CKI CERNER!07B2090C-7AE6-4E14-A702-C20EE3E7D4FD for the associated child. |
| 40 | `NEONATE_COMPLICATION_GROUP_ID` | DOUBLE |  | FK→ | foreign key to whc_d_complication_group.whc_d_complication_group_id, representing a combination of neonatal complication types for the child in context. |
| 41 | `NEONATE_DISCHARGE_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE corresponding to ENCOUNTER.DISCH_DT_TM for the associated child's encounter created when the delivery took place (between delivery date time for the associated pregnancy and the pregnancy close date time). |
| 42 | `NEONATE_DISCHARGE_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME corresponding to ENCOUNTER.DISCH_DT_TM for the associated child's encounter created when the delivery took place (between delivery date time for the associated pregnancy and the pregnancy close date time). |
| 43 | `NEONATE_IN_NURSERY_REQUESTS` | VARCHAR(255) |  |  | User-readable description of 'Requests for Neonate in Nursery' value, taken from the clinical result recorded against CKI CERNER!CF2C6051-A4BE-4294-B7DE-F1E7A8C8D80F for the associated child. |
| 44 | `NEONATE_OUTCOME_DESC` | VARCHAR(255) |  |  | Display value of PREGNANCY_CHILD.NEONATE_OUTCOME_CD for the associated child, representing the outcome of the pregnancy for the child. |
| 45 | `NEONATE_OUTPUT_DESC` | VARCHAR(255) |  |  | User-readable description of 'Newborn Output' value, taken from the clinical result recorded against CKI CERNER!135F4B41-C499-4EFC-BE49-779D5C9CA487 for the associated child. |
| 46 | `NEWBORN_INTAKE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_INTAKE_TYPE.WHC_D_INTAKE_TYPE_ID, representing the intake type for the associated child. |
| 47 | `NUCHAL_CORD_INTERVENTION_DESC` | VARCHAR(255) |  |  | User-readable description of 'Nuchal Cord Interventions' value, taken from the clinical result recorded against CKI CERNER!16007E61-699F-478F-9FDC-8D66E3B880A1 for the associated child. |
| 48 | `NUCHAL_CORD_TENSION_DESC` | VARCHAR(255) |  |  | User-readable description of 'Nuchal Cord Tension' value, taken from the clinical result recorded against CKI CERNER!9746FC5D-DD49-4B55-8036-508FC5448833 for the associated child. |
| 49 | `NUCHAL_CORD_TIMES_WRAPPED_NBR` | DOUBLE |  |  | User-readable description of 'Nuchal Cord Times' value, taken from the clinical result recorded against CKI CERNER!BA37C2F7-8376-4D2F-B7F6-59B262E5FCB7 for the associated child. |
| 50 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_F_ORGANIZATION.WHC_D_ORGANIZATION_ID, for the organization responsible for the child's care. |
| 51 | `PRETERM_SS_DESC` | VARCHAR(255) |  |  | Same value as for WHC_F_DELIVERY.PRETERM_SS_DESC |
| 52 | `RESUS_AT_BIRTH_DESC` | VARCHAR(255) |  |  | User-readable description of 'Resuscitation at Birth' value, taken from the clinical result recorded against CKI CERNER!932A8EBA-84AD-4412-8741-240A9810337E for the associated child. |
| 53 | `SEX_OF_CHILD_DESC` | VARCHAR(40) |  |  | User-readable description of 'Gender' value, taken from the clinical result recorded against CKI CERNER!ASYr9AEYvUr1YoQ0CqIGfQ for the associated child. |
| 54 | `SKIN_SKIN_CONTCT_INT_DATE_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_DATE, corresponding to the clinical result recorded against CKI CERNER!E0522A70-AC79-4F21-A52D-A52155B7D727 for the associated child. This CKI corresponds to the 'Skin to Skin Contact Initiated' event date/time. |
| 55 | `SKIN_SKIN_CONTCT_INT_TIME_NBR` | DOUBLE | NOT NULL | FK→ | Foreign key to OMF_TIME, corresponding to the clinical result recorded against CKI CERNER!E0522A70-AC79-4F21-A52D-A52155B7D727 for the associated child. This CKI corresponds to the 'Skin to Skin Contact Initiated' event date/time. |
| 56 | `SPONTANEOUS_RESP_ONSET_DESC` | VARCHAR(255) |  |  | User-readable description of 'Spontaneous Respirations Onset' value, taken from the clinical result recorded against CKI CERNER!27BFCBFC-17A7-4254-B2F0-530483CC8990 for the associated child. |
| 57 | `TRANSACTION_PROFILE_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to WHC_D_TRANSACTION_PROFILE.WHC_D_TRANSACTION_PROFILE_ID. |
| 58 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 59 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 60 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 61 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 62 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 63 | `WHC_F_CHILD_ID` | DOUBLE | NOT NULL |  | Primary Key |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ABDOMINAL_CIRCUMFRNCE_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `ANESTHESIA_GROUP_ID` | [WHC_D_ANESTHESIA_GROUP](WHC_D_ANESTHESIA_GROUP.md) | `WHC_D_ANESTHESIA_GROUP_ID` |
| `BIRTH_HEIGHT_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `BIRTH_WEIGHT_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `CHEST_CIRCUMFERENCE_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `CHILD_BIRTH_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `CHILD_BIRTH_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `CHILD_ID` | [WHC_D_PERSON](WHC_D_PERSON.md) | `WHC_D_PERSON_ID` |
| `DELIVERY_TYPE_ID` | [WHC_D_DELIVERY_TYPE](WHC_D_DELIVERY_TYPE.md) | `WHC_D_DELIVERY_TYPE_ID` |
| `FETAL_COMPLICATION_GROUP_ID` | [WHC_D_COMPLICATION_GROUP](WHC_D_COMPLICATION_GROUP.md) | `WHC_D_COMPLICATION_GROUP_ID` |
| `HEAD_CIRCUMFERNENCE_UOM_ID` | [WHC_D_UOM_TYPE](WHC_D_UOM_TYPE.md) | `WHC_D_UOM_TYPE_ID` |
| `MOTHER_ID` | [WHC_D_PERSON](WHC_D_PERSON.md) | `WHC_D_PERSON_ID` |
| `NEONATE_ADMISSION_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `NEONATE_ADMISSION_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `NEONATE_COMPLICATION_GROUP_ID` | [WHC_D_COMPLICATION_GROUP](WHC_D_COMPLICATION_GROUP.md) | `WHC_D_COMPLICATION_GROUP_ID` |
| `NEONATE_DISCHARGE_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `NEONATE_DISCHARGE_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `NEWBORN_INTAKE_TYPE_ID` | [WHC_D_INTAKE_TYPE](WHC_D_INTAKE_TYPE.md) | `WHC_D_INTAKE_TYPE_ID` |
| `ORGANIZATION_ID` | [WHC_D_ORGANIZATION](WHC_D_ORGANIZATION.md) | `WHC_D_ORGANIZATION_ID` |
| `SKIN_SKIN_CONTCT_INT_DATE_NBR` | [OMF_DATE](OMF_DATE.md) | `DT_NBR` |
| `SKIN_SKIN_CONTCT_INT_TIME_NBR` | [OMF_TIME](OMF_TIME.md) | `MIN_NBR` |
| `TRANSACTION_PROFILE_ID` | [WHC_D_TRANSACTION_PROFILE](WHC_D_TRANSACTION_PROFILE.md) | `WHC_D_TRANSACTION_PROFILE_ID` |

