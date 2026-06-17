# SN_CT_DISPLAY_FIELD

> Stores the individual piees of data and their sequence on a row in the case tracking dynamic view

**Description:** Surginet Case Tracking Display Field  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FIELD_PROMPT` | VARCHAR(50) |  |  | Field PromptColumn |
| 2 | `FIELD_SEQUENCE` | DOUBLE | NOT NULL |  | Determines the order in which fields with the same sn_ct_display_row_id will appear |
| 3 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Defines what piece of data from the surgical case the field should contain. |
| 4 | `PARENT_ENTITY_NAME` | VARCHAR(32) |  |  | Describes the source of the parent_entity_id |
| 5 | `SN_CT_DISPLAY_FIELD_ID` | DOUBLE | NOT NULL |  | Primary key for this table |
| 6 | `SN_CT_DISPLAY_ROW_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to indicate which display row this field belongs to. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SN_CT_DISPLAY_ROW_ID` | [SN_CT_DISPLAY_ROW](SN_CT_DISPLAY_ROW.md) | `SN_CT_DISPLAY_ROW_ID` |

