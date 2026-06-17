# EXT_REQ_STATUS

> Table to store the third party request for ENT project.

**Description:** External Request Status  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 28

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCOUNT_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the ACCOUNT table.a |
| 2 | `BEG_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 3 | `BILL_VRSN_NBR` | DOUBLE | NOT NULL | FK→ | The version number identifying which bill |
| 4 | `BO_HP_RELTN_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the BO_HP_RELTN table. |
| 5 | `CORSP_ACTIVITY_ID` | DOUBLE | NOT NULL | FK→ | Combined with the BILL_VRSN_NBR column uniquely identifies a related row on the BILL_REC table. |
| 6 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the related row on the Encounter table. |
| 7 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 8 | `EVENT_CD` | DOUBLE | NOT NULL |  | Contains the event code that will be published through the request.; |
| 9 | `EVENT_DT_TM` | DATETIME |  |  | Event date when requested action was created. |
| 10 | `EVENT_NAME` | VARCHAR(252) | NOT NULL |  | Name used by the system to identify a specific event. |
| 11 | `EVENT_TITLE_TXT` | VARCHAR(252) | NOT NULL |  | Name used to display the name of the identified event. |
| 12 | `EVENT_URL` | VARCHAR(252) | NOT NULL |  | URL associated to the requested event occurrence. |
| 13 | `EXT_REQ_CLOB` | LONGTEXT |  |  | External request payload data from the third party request coming from HDX |
| 14 | `EXT_REQ_IDENT` | VARCHAR(250) |  |  | External request identifier from the third party request coming from HDX |
| 15 | `EXT_REQ_STATUS_CD` | DOUBLE | NOT NULL |  | External request status code to indicate the status of the request. |
| 16 | `EXT_REQ_STATUS_ID` | DOUBLE | NOT NULL |  | External request identifier from the third party request coming from HDX |
| 17 | `EXT_REQ_STATUS_REASON_TXT` | VARCHAR(250) |  |  | External request status reason to indicate the reason of the request status |
| 18 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | Uniquely identifies the Person_ID on the Person table to which the requested event is associated.; |
| 19 | `PUBLISHER_CONTACT_INFO_TXT` | VARCHAR(255) |  |  | Contains the Publishers contact information |
| 20 | `PUBLISHER_IDENT` | DOUBLE | NOT NULL |  | ** OBSOLETE ** This column is no longer being used. It has been replaced by Publisher_txt_ident. External Unique Identifier of the Publisher Organization. ** OBSOLETE ** |
| 21 | `PUBLISHER_NAME` | VARCHAR(252) | NOT NULL |  | Name of the publisher (organization or potentially an individual) |
| 22 | `PUBLISHER_TXT_IDENT` | VARCHAR(255) |  |  | Unique Identifier of the publisher of the request, its ALPHA numeric value from 3rd part application. |
| 23 | `TASK_TYPE_TXT` | VARCHAR(252) | NOT NULL |  | Contains the type of the task that is requested for processing. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACCOUNT_ID` | [ACCOUNT](ACCOUNT.md) | `ACCT_ID` |
| `BILL_VRSN_NBR` | [BILL_REC](BILL_REC.md) | `BILL_VRSN_NBR` |
| `BO_HP_RELTN_ID` | [BO_HP_RELTN](BO_HP_RELTN.md) | `BO_HP_RELTN_ID` |
| `CORSP_ACTIVITY_ID` | [BILL_REC](BILL_REC.md) | `CORSP_ACTIVITY_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

