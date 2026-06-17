# CT_PT_SETTINGS

> This table holds whether a patient is interested in being pre-screened for clinical trial protocols.

**Description:** Patient/Trial Pre-screening Settings table.  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 12

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `CT_PT_SETTINGS_ID` | DOUBLE | NOT NULL |  | Primary key of the table. It is a system assigned number ( protocol_def_seq) |
| 3 | `INTEREST_OPTION_CD` | DOUBLE | NOT NULL |  | Interest option code value associated with the patient interest |
| 4 | `NOT_INTERESTED_DT_TM` | DATETIME |  |  | Date and time the Not Interested Indicator was set. |
| 5 | `NOT_INTERESTED_IND` | DOUBLE | NOT NULL |  | This field contains the code identifying the pre-screening status of the potential trial candidate for the protocol. |
| 6 | `NOT_INTERESTED_PRSNL_ID` | DOUBLE | NOT NULL |  | Prsnl updating not interested data |
| 7 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | The person who does or does not have interest in being pre-screened for any clinical trial protocols. This is the value of the unique primary identifier of the person table for the person who has their interest for being pre-screened for Clinical Trials protocols indicated in this table. It is an internal system assigned number. |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

