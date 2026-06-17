# UKRWH_MSDS_DETAILS

> Contains pregnancy, fetus and birth activity details from NHS Maternity Services Data Set.

**Description:** UKRWH_MSDS_DETAILS  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `EXTRACT_DT_TM` | DATETIME |  |  | Date and Time of when extract was created. |
| 3 | `FIRST_PROCESS_DT_TM` | DATETIME |  |  | First date/time row was inserted into table. |
| 4 | `HEALTH_SYSTEM_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the health system. |
| 5 | `HEALTH_SYSTEM_SOURCE_ID` | DOUBLE | NOT NULL |  | Unique number assigned by Health Facts. Typically the universal Cerner assigned client id of the sending health system but may be adjusted if there is >1 HF feed from the client. |
| 6 | `LAST_PROCESS_DT_TM` | DATETIME |  |  | Last date/time row was updated. |
| 7 | `LOC_MSDS_VALUE_IN_DT_TM` | DATETIME |  |  | Value in date and time converted to local datetime. |
| 8 | `MSDS_DETAILS_SEQUENCE` | DOUBLE |  |  | Sequence of occurrence. |
| 9 | `MSDS_ELEMENT` | VARCHAR(100) |  |  | Maternity Services Data Set element Description. |
| 10 | `MSDS_ELEMENT_GROUP_DESC` | VARCHAR(100) |  |  | Maternity Services Data Set (MSDS) group element description. |
| 11 | `MSDS_ELEMENT_GROUP_NO` | VARCHAR(20) |  |  | Maternity Services Data Set (MSDS) group element number. |
| 12 | `MSDS_PARENT_ELEMENT_DESC` | VARCHAR(100) |  |  | Maternity Services Data Set (MSDS) parent element description. |
| 13 | `MSDS_PARENT_ELEMENT_NO` | VARCHAR(20) |  |  | Maternity Services Data Set (MSDS) parent element number. |
| 14 | `MSDS_VALUE` | VARCHAR(100) |  |  | Value of Maternity Services Data Set (MSDS) element. |
| 15 | `MSDS_VALUE_IN_NBR` | DOUBLE |  |  | Value in number. |
| 16 | `MSDS_VALUE_IN_NHS` | VARCHAR(100) |  |  | Value in NHS reference code. |
| 17 | `MSDS_VALUE_TYPE_DESC` | VARCHAR(100) |  |  | Reference value type description - NHS reference code, Number, Date or String. |
| 18 | `PARENT_ENTITY_KEY` | DOUBLE |  |  | PIEDW system generated unique identifier for a pregnancy or fetus. |
| 19 | `PARENT_ENTITY_NAME` | VARCHAR(100) |  |  | Parent type of entity - pregnancy or fetus. |
| 20 | `PARENT_ENTITY_SK` | VARCHAR(40) |  |  | Millennium system generated unique identifier for a pregnancy or fetus. |
| 21 | `TOTAL_UPDATES` | DOUBLE |  |  | The numbers of updates that have occurred on this table. |
| 22 | `UKRWH_MSDS_DETAILS_KEY` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the UKRWH_MSDS_DETAILS table. |
| 23 | `UPDT_CNT` | DOUBLE |  |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME |  |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_TASK` | VARCHAR(40) |  |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 26 | `UPDT_USER` | VARCHAR(40) |  |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

