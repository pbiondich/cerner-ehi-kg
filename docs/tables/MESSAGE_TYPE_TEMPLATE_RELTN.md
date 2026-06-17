# MESSAGE_TYPE_TEMPLATE_RELTN

> Stores the association between a message type and its associated templates

**Description:** Message-Type Template Relatioin  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 10

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DEFAULT_IND` | DOUBLE | NOT NULL |  | This is to indicate which template is the default for a given message type |
| 2 | `MED_IND` | DOUBLE | NOT NULL |  | This indicator is going to decide whether the message is going to route to the renewal request folder or not. 0 - don't route1 - route |
| 3 | `MESSAGE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | The Message Type Cd for the message type that has an associated template |
| 4 | `MESSAGE_TYPE_TEMPLATE_RELTN_ID` | DOUBLE | NOT NULL |  | Primary key to index an association between a message type and a template |
| 5 | `TEMPLATE_ID` | DOUBLE | NOT NULL | FK→ | The Template Id for the Template that has an association to the message type. FK from Clinical Note Template. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MESSAGE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TEMPLATE_ID` | [CLINICAL_NOTE_TEMPLATE](CLINICAL_NOTE_TEMPLATE.md) | `TEMPLATE_ID` |

