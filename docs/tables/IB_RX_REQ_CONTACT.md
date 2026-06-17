# IB_RX_REQ_CONTACT

> Stores the contact information for the patient on the inbound pharmacy request.

**Description:** Inbound Rx Request Contact  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EMAIL_ADDR` | VARCHAR(255) |  |  | The patient's email address provided on the inbound request. |
| 2 | `IB_RX_REQ_CONTACT_ID` | DOUBLE | NOT NULL |  | Unique, generated number that is used to identify an individual row on the IB_RX_REQ_CONTACT table. |
| 3 | `IB_RX_REQ_PERSON_DEMOG_ID` | DOUBLE | NOT NULL | FK→ | Relationship to the person this contact information is for. |
| 4 | `PHONE_NBR_TXT` | VARCHAR(255) |  |  | The phone number of the patient identified on the inbound request. |
| 5 | `PHONE_NBR_TYPE_CD` | DOUBLE | NOT NULL |  | The type of phone of the associated phone number. Ex. Cell, home. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `IB_RX_REQ_PERSON_DEMOG_ID` | [IB_RX_REQ_PERSON_DEMOG](IB_RX_REQ_PERSON_DEMOG.md) | `IB_RX_REQ_PERSON_DEMOG_ID` |

