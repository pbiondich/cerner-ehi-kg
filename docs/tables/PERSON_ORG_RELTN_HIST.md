# PERSON_ORG_RELTN_HIST

> Used to store transactional history for person organization relationships.

**Description:** Person Organization Relation History  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 39

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CHANGE_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 7 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 8 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 9 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 10 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 11 | `EMPL_CONTACT` | VARCHAR(100) |  |  | The name of the person at the employer organization to verify employment. |
| 12 | `EMPL_HIRE_DT_TM` | DATETIME |  |  | The date the employee was hired. |
| 13 | `EMPL_OCCUPATION_CD` | DOUBLE | NOT NULL |  | The codified representation of the person's type of work performed on behalf of the employer organization. |
| 14 | `EMPL_OCCUPATION_NOMEN_ID` | DOUBLE |  | FK→ | The identifying information of the nomenclature defining the person's type of work performed on behalf of the employer organization. Examples may include Bank Officer, Java Software Developer, and Nurse Practitioner. |
| 15 | `EMPL_OCCUPATION_TEXT` | VARCHAR(100) |  |  | The textual description of the person's type of work performed on behalf of the employer organization. |
| 16 | `EMPL_OCC_INDUSTRY_NOMEN_ID` | DOUBLE |  | FK→ | The identifying information of the nomenclature defining the type of business that compensates the person for work or assigns work to the person as an unpaid worker or volunteer. Examples may include Federal Savings Banks, Computer Software Support Services, and Pharmacies. |
| 17 | `EMPL_POSITION` | VARCHAR(100) |  |  | The work position given to the employee by the employer organization. |
| 18 | `EMPL_RETIRE_DT_TM` | DATETIME |  |  | The date the employee retired. |
| 19 | `EMPL_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates a condition of employment (i.e. probation, leave, employed, terminated). |
| 20 | `EMPL_TERM_DT_TM` | DATETIME |  |  | Date the employee was terminated. |
| 21 | `EMPL_TITLE` | VARCHAR(100) | NOT NULL |  | Employee title is the work title given to the employee by the employer organization. |
| 22 | `EMPL_TITLE_CD` | DOUBLE | NOT NULL |  | Employee title code is the codified work title given to the employee by the employer organization. |
| 23 | `EMPL_TYPE_CD` | DOUBLE | NOT NULL |  | Employee type identifies the kind of employment related to the number of hours worked and/or how the employee is paid (I.e., part time-hourly, full time-salary, etc.). |
| 24 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 25 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the organization table. It is an internal system assigned number. |
| 26 | `PERSON_ORG_NBR` | VARCHAR(100) |  |  | This is the primary external identifier for the person organization relationship (I.e., employee number, student id number, etc.) |
| 27 | `PERSON_ORG_RELTN_CD` | DOUBLE | NOT NULL |  | Identifies the specific type of relationship of the person to the organization. This field has Cerner defined meanings (I.e., employee, student, etc.) |
| 28 | `PERSON_ORG_RELTN_HIST_ID` | DOUBLE | NOT NULL |  | The primary key of the PERSON_ORG_RELTN_HIST table. |
| 29 | `PERSON_ORG_RELTN_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person organization relationship table. It is an internal system assigned number. |
| 30 | `PM_HIST_TRACKING_ID` | DOUBLE | NOT NULL | FK→ | This is the unique primary identifier of the pm_hist_tracking table. It is an internal system assigned number. |
| 31 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Identifies a sequencing priority to be used when a duplicate relationship of the same type is created. |
| 32 | `SOURCE_IDENTIFIER` | VARCHAR(255) |  |  | Identifier assigned from a master system to this row. Added to support the uk's pds allocated object identifier. Used to help keep the uk master in sync with millennium. |
| 33 | `TRACKING_BIT` | DOUBLE | NOT NULL |  | Identifies which columns have had a change. |
| 34 | `TRANSACTION_DT_TM` | DATETIME | NOT NULL |  | ** OBSOLETE **. Use column updt_dt_tm for any filtering/ordering query. If transaction date time is needed, it should be retrieved from pm_hist_tracking table. Note that its date may be in the past, as in before the update date time. |
| 35 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 36 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 37 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 38 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 39 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `EMPL_OCCUPATION_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `EMPL_OCC_INDUSTRY_NOMEN_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `PERSON_ORG_RELTN_ID` | [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `PERSON_ORG_RELTN_ID` |
| `PM_HIST_TRACKING_ID` | [PM_HIST_TRACKING](PM_HIST_TRACKING.md) | `PM_HIST_TRACKING_ID` |

