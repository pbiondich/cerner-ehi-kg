# ESO_TRIGHOLD_RULE

> Stores rules for combining currently held triggers with incoming triggers.

**Description:** ESO Trigger Hold Rule  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 9

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLASS` | VARCHAR(15) | NOT NULL |  | The trigger's CQM class |
| 2 | `DOUBLE_LIST_NAME` | VARCHAR(40) | NOT NULL |  | Defines the rule for combining triggers |
| 3 | `ESO_TRIGHOLD_RULE_ID` | DOUBLE | NOT NULL |  | Defines a unique ID for each trigger hold rule |
| 4 | `SEQ_NBR` | DOUBLE | NOT NULL |  | Sequence number of double list entry |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

