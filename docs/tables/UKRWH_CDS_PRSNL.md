# UKRWH_CDS_PRSNL

> Contains Personnel details.

**Description:** UK Reporting Warehouse Commissioning Data Set Personnel  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_PRSNL` | VARCHAR(40) |  |  | The person who caused the active_status_cd to be set or change. |
| 3 | `CONSULTANT_CODE_IDENT` | VARCHAR(15) |  |  | This is the GENERAL MEDICAL COUNCIL (GMC) NUMBER for the CONSULTANT. For GENERAL MEDICAL PRACTITIONERS working as CONSULTANTS, the GENERAL MEDICAL PRACTITIONER's GENERAL MEDICAL COUNCIL (GMC) NUMBER should be used, see data item note for GENERAL MEDICAL PRACTITIONER (SPECIFIED). |
| 4 | `FIRST_NAME` | VARCHAR(200) |  |  | The specific first name of a patient by which a PERSON may be known. |
| 5 | `FIRST_NAME_UNF` | VARCHAR(200) |  |  | This is the person's first given name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 6 | `FIRST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the first process |
| 7 | `FULL_FORMATTED_NAME` | VARCHAR(200) |  |  | This is the complete person name including punctuation and formatting. |
| 8 | `GP_CODE_IDENT` | VARCHAR(15) |  |  | This is the code of the GENERAL MEDICAL PRACTITIONER specified by the PATIENT. |
| 9 | `HEALTH_SYSTEM_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 10 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE |  |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 11 | `LAST_NAME` | VARCHAR(200) |  |  | The specific surname / last name of a patient by which a PERSON may be known. |
| 12 | `LAST_NAME_UNF` | VARCHAR(200) |  |  | This is the person's family name all capitals with punctuation removed. This field is used for indexing and searching for a person by name. |
| 13 | `LAST_PROCESS_DT_TM` | DATETIME | NOT NULL |  | Date and time of the second process |
| 14 | `MIDDLE_NAME` | VARCHAR(200) |  |  | The specific middle name of a patient by which a PERSON may be known. |
| 15 | `MILL_USERNAME` | VARCHAR(50) |  |  | The system user name for the personnel used to gain primary access to the computer system. |
| 16 | `PHYSICIAN_IND` | DOUBLE |  |  | Set to TRUE, if the personnel is a physician. Otherwise, set to FALSE. |
| 17 | `POSITION_DISPLAY_TXT` | VARCHAR(40) |  |  | The Display text of the position that was used to determine the applications and tasks the personnel is authorized to use. |
| 18 | `POSITION_REF` | VARCHAR(40) |  |  | The position is used to determine the applications and tasks the personnel is authorized to use. |
| 19 | `PREFIX_NAME` | VARCHAR(100) |  |  | Name prefix includes any titles that will precede the regular person name. |
| 20 | `PRSNL_CODE_IDENT` | VARCHAR(100) |  |  | Personnel Id associated with routing rule |
| 21 | `PRSNL_PERSON_SK` | VARCHAR(40) |  |  | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 22 | `TOTAL_UPDATES` | DOUBLE | NOT NULL |  | The numbers of updates that have occurred on this table. |
| 23 | `UKRWH_CDS_PRSNL_KEY` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the ukrwh cds prsnl table. It is an internal system assigned number. |
| 24 | `UPDATE_USER` | VARCHAR(40) | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

