# MM_MP_WORKLIST_FILTER

> Stores the filters for Supply Chain Mpage Worklist. Filters are stored based off User + View/Workflow.

**Description:** Supply CHain MPages Worklist Filter  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Refers PERSON_ID from PRSNL table. Stores the ID of User who define the filter template details. |
| 2 | `FILTER_TEMPLATE_NAME` | VARCHAR(255) | NOT NULL |  | Name of the Filter Template |
| 3 | `GLOBAL_FILTER_IND` | DOUBLE | NOT NULL |  | Indicator value would be set to 1 for the filters that are available for all the users per view. Indicator value would be set to 0 for the user's personal filters. |
| 4 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | LONG_TEXT_ID from long_text_reference table that refers to the filter details stored |
| 5 | `MM_MP_WORKLIST_FILTER_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the MM_MP_WORKLIST_FILTER table. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VIEW_IDENTIFIER_TXT` | VARCHAR(30) | NOT NULL |  | View Identifier created in Bedrock for the Mpages view |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `LONG_TEXT_ID` | [LONG_TEXT_REFERENCE](LONG_TEXT_REFERENCE.md) | `LONG_TEXT_ID` |

