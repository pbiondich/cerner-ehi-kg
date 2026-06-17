# MAMMO_STUDY

> Master record for Mammography follow up case.

**Description:** Mammography Study  
**Table type:** ACTIVITY  
**Primary key:** `STUDY_ID`  
**Columns:** 35  
**Referenced by:** 15 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ASSESSMENT_ID` | DOUBLE | NOT NULL | FK→ | The Radiologist's case assessment. This is a foreign key to the Rad_Fol_Up_Field table. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | Identifies the mammography procedure |
| 4 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 5 | `DATA_CAPTURE_FLAG` | DOUBLE | NOT NULL |  | tell whether the examination is done at the combination level or component level.0 = Default, 1 = Combination level, 2 = Component level |
| 6 | `DOWNLOAD_IND` | DOUBLE |  |  | This column indicates whether or not the study has been previously downloaded for the acr birads national mammography database. A 1 indicates that it has been downloaded. |
| 7 | `EDITION_NBR` | DOUBLE | NOT NULL |  | This column stores the ACR BI-RADS edition that the study falls under. Edition 2 and edition 3 do not have decimal precision and will be assumed to mean 2.0 and 3.0. Starting with edition 3.1, the edition number appearing in the column on the table will be assumed to have a single decimal precision. In other words, edition 3.1 will be appear as 31 on the table. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 9 | `EXCLUDE_FROM_AUDIT_IND` | DOUBLE | NOT NULL |  | Indicates if case should be excluded from audit statistics |
| 10 | `GROUP_REFERENCE_NBR` | VARCHAR(40) |  |  | This is used along with the contributor_system_cd to uniquely identify the report that corresponds with this case. |
| 11 | `INCLUDE_BREAST_DENSITY_IND` | DOUBLE |  |  | This column will contain value of include breast density statement indicator value, as saved by user in Mammo case maintenance. If this is set to Yes, then the breast density statement set for the selected facility in breast_density_text in Rad_Config_Data table will be printed in mammo notification letters. If this is set to No or blank, then the set breast density statement will not be printed in the mammo notification letters. |
| 12 | `LATERALITY_AUDIT_FLAG` | DOUBLE | NOT NULL |  | tells whether the exam is being done at the separate breast level or at the patient level. 0 = Default, 1 = Patient level assessment, 2 = Separate breast level assessment. |
| 13 | `LETTER_ID` | DOUBLE | NOT NULL | FK→ | This is the Letter Id of the letter currently assigned to the study |
| 14 | `MAMMO_IMAGING_FLAG` | DOUBLE | NOT NULL |  | Indicates how the facility defines standard screeningmammography images |
| 15 | `MAPPED_ACTIVITY_SUBTYPE_CD` | DOUBLE | NOT NULL |  | Indicates which modality the particular study belongs to. |
| 16 | `NO_FOL_UP_REQ_IND` | DOUBLE |  |  | If this field is 1, a follow up is not required. If it is 0 or NULL then a follow up is required. |
| 17 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | This is a foreign key to the Order Radiology table. It identifies the order that the follow-up case is related to. |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 19 | `REASON_ID` | DOUBLE | NOT NULL | FK→ | Reason for the Mammography procedure. This is a foreign key to the Rad_Fol_Up_Field table. |
| 20 | `RECALL_INTERVAL` | DOUBLE |  |  | The recall interval in months |
| 21 | `RECOMMENDATION_ID` | DOUBLE | NOT NULL | FK→ | The Radiologist's recommendation for follow-up (ACR). This is a foreign key to the Rad_Fol_Up_Field table. Choices depend on Assessment_Id |
| 22 | `REPRINT_IND` | DOUBLE | NOT NULL |  | This column is used to identify whether the study should be included for reprint when we run the ops job for the patient notification letter. Mainly used for linked exams. 0 - do not reprint. 1 - reprint. |
| 23 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | FK→ | In the case of historical uploads, this field will be filled out with the seq_exam_id of the exam (exam_data) that the mammo data was uploaded with. If the study was not uploaded this will remain Null |
| 24 | `STAT_CAT_FLAG` | DOUBLE |  |  | This column stores the statistical category flag for the study. |
| 25 | `STAT_CAT_ID` | DOUBLE | NOT NULL | FK→ | the Cases statistical category. This is a foreign key to the Rad_Fol_Up_Field table. |
| 26 | `STUDY_DT_TM` | DATETIME |  |  | The date and time that the mammogram was performed. |
| 27 | `STUDY_ID` | DOUBLE | NOT NULL | PK | This column serves as a unique identifier for the row. It is meaningless other than to uniquely identify the row. |
| 28 | `STUDY_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 29 | `SUBSECTION_CD` | DOUBLE | NOT NULL | FK→ | Subsection in which the exam was performed |
| 30 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 31 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 32 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 33 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 34 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 35 | `US_IMAGING_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the facility defines standard screeningultrasound images . |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ASSESSMENT_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `LETTER_ID` | [MAMMO_LETTER](MAMMO_LETTER.md) | `LETTER_ID` |
| `ORDER_ID` | [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |
| `REASON_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `RECOMMENDATION_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `SEQ_EXAM_ID` | [EXAM_DATA](EXAM_DATA.md) | `SEQ_EXAM_ID` |
| `STAT_CAT_ID` | [RAD_FOL_UP_FIELD](RAD_FOL_UP_FIELD.md) | `FOLLOW_UP_FIELD_ID` |
| `SUBSECTION_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |

## Referenced by (15)

| From table | Column |
|------------|--------|
| [MAMMO_ASSESSMENT_SERIES](MAMMO_ASSESSMENT_SERIES.md) | `STUDY_ID` |
| [MAMMO_BREAST_FIND](MAMMO_BREAST_FIND.md) | `STUDY_ID` |
| [MAMMO_FOLLOW_UP](MAMMO_FOLLOW_UP.md) | `STUDY_ID` |
| [MAMMO_NOTIFICATION](MAMMO_NOTIFICATION.md) | `STUDY_ID` |
| [MAMMO_NOTIFICATION_HIST](MAMMO_NOTIFICATION_HIST.md) | `STUDY_ID` |
| [MAMMO_PROBLEM](MAMMO_PROBLEM.md) | `STUDY_ID` |
| [MAMMO_RECOMMEND_SEQ](MAMMO_RECOMMEND_SEQ.md) | `STUDY_ID` |
| [MAMMO_RECOMMEND_SERIES](MAMMO_RECOMMEND_SERIES.md) | `STUDY_ID` |
| [MAMMO_RISK](MAMMO_RISK.md) | `STUDY_ID` |
| [MAMMO_STUDY_PRSNL](MAMMO_STUDY_PRSNL.md) | `STUDY_ID` |
| [MAMMO_USER_DEF](MAMMO_USER_DEF.md) | `STUDY_ID` |
| [RAD_MAMMO_STUDY_ASSESS_MGMT_R](RAD_MAMMO_STUDY_ASSESS_MGMT_R.md) | `STUDY_ID` |
| [RAD_OMF_MAMMO](RAD_OMF_MAMMO.md) | `STUDY_ID` |
| [RAD_OMF_MAMMO_DETAILS](RAD_OMF_MAMMO_DETAILS.md) | `STUDY_ID` |
| [RAD_OMF_MAMMO_FIND](RAD_OMF_MAMMO_FIND.md) | `STUDY_ID` |

