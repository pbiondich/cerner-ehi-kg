# HIM_REQUEST_TEMPLATE_R

> This table stores the relationship between HIM Requests and the letters to be printed for each status of the request.

**Description:** HIM Request/Letters to be printed relationships.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 2 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 3 | `HIM_REQUEST_TEMPLATE_R_ID` | DOUBLE | NOT NULL |  | Primary Key - system generated - uniquely identifies a row in the table |
| 4 | `LETTER_TYPE_CD` | DOUBLE | NOT NULL |  | Identified the type of letter that the template will be used for. |
| 5 | `REQUEST_STATUS_CD` | DOUBLE | NOT NULL |  | The status of the request to which the letter template needs to be associated |
| 6 | `REQUEST_TYPE_CD` | DOUBLE | NOT NULL |  | Identifies the type of request for which the letter template would be used to print letters |
| 7 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | Identifies the letter template which is to be associated with the request status |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `TEMPLATE_ID` | [WP_TEMPLATE](WP_TEMPLATE.md) | `TEMPLATE_ID` |

