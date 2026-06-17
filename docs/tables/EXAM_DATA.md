# EXAM_DATA

> The Exam_Data table contains common information about a radiology exam that was performed.

**Description:** Exam Data  
**Table type:** ACTIVITY  
**Primary key:** `SEQ_EXAM_ID`  
**Columns:** 22  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The Catalog_Cd is a foreign key to the Order_Catalog table. This identifies which exam was performed. |
| 2 | `COMPLETE_DT_TM` | DATETIME |  |  | The Complete_Dt_Tm captures the date and time that the exam was performed. |
| 3 | `COMPLETE_LOCN_CD` | DOUBLE | NOT NULL |  | The Complete_Locn_Cd captures the unique id for the exam room in which the exam was performed. |
| 4 | `COMPLETE_TZ` | DOUBLE |  |  | Time zone associated with the corresponding DT_TM column. |
| 5 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 7 | `FLUORO_MINS_USED` | DOUBLE |  |  | This column contains the number of minutes that fluoro was used during the exam. |
| 8 | `GROUP_REFERENCE_NBR` | VARCHAR(40) |  |  | The Group_Reference_Nbr serves as a tie to the corresponding row in the repository. |
| 9 | `MEDICAL_LEGAL_IND` | DOUBLE |  |  | The Medical_Legal_Ind identifies those exam that have medical legal implications. |
| 10 | `MED_LEGAL_CMNT` | VARCHAR(255) |  |  | The Medical_Legal_Cmnt field contains any comments relevant to the exams medical legal status. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order Id from the orders table |
| 12 | `OUTSIDE_CASE_IND` | DOUBLE |  |  | This column indicates if the row on the exam_data table represents an outside case. This is used for interesting cases. |
| 13 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 14 | `PURGE_IND` | DOUBLE |  |  | The Purge_Ind indicates whether or not an exam has been marked for purge. |
| 15 | `READ_COMPLETE_IND` | DOUBLE |  |  | The Read_Complete_Ind indicates whether or not the exam has been interpreted by the radiologist/resident. |
| 16 | `REPORT_ID` | DOUBLE | NOT NULL |  | The Report_Id is a foreign key to the Clinical Event table. This serves as the tie between the exam within image management and the report in the repository. |
| 17 | `SEQ_EXAM_ID` | DOUBLE | NOT NULL | PK | The Seq_Exam_Id uniquely identifies a row within the Exam_Data table. It has no other meaning or purpose other than to serve as a unique id. |
| 18 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 19 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [FILM_EXAM](FILM_EXAM.md) | `SEQ_EXAM_ID` |
| [MAMMO_STUDY](MAMMO_STUDY.md) | `SEQ_EXAM_ID` |
| [MEDIA_EXAM](MEDIA_EXAM.md) | `SEQ_EXAM_ID` |
| [ORDER_RADIOLOGY](ORDER_RADIOLOGY.md) | `SEQ_EXAM_ID` |
| [RAD_EXPOSURE](RAD_EXPOSURE.md) | `SEQ_EXAM_ID` |
| [RAD_INT_CASE_R](RAD_INT_CASE_R.md) | `SEQ_EXAM_ID` |
| [TEMPORARY_EXAM](TEMPORARY_EXAM.md) | `SEQ_EXAM_ID` |

