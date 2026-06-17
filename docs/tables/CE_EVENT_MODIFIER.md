# CE_EVENT_MODIFIER

> The ce_event_modifier table stores items which apply to a clinical event. For instance, a modifier for a blood pressure reading may be the orientation of the person during the reading (sitting, standing?).

**Description:** The ce_event_modifier table stores items which apply to a clinical event. For i  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 15

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `EVENT_ID` | DOUBLE | NOT NULL |  | Foreign key to clinical_event table. |
| 2 | `GROUP_SEQUENCE` | DOUBLE |  |  | Maps groups of items into separate sets for display and ordering purposes. Starts at 0 and can have only positive values (0-n) |
| 3 | `ITEM_SEQUENCE` | DOUBLE |  |  | Maps the Items within a group to a unique identifier for ordering purposes. Starts at 0 and can have only positive values (0-n) |
| 4 | `MODIFIER_CD` | DOUBLE | NOT NULL |  | Indicates the type of modifier. This code value will imply a code set for the modifier_value_cd field. I have not yet created a code set for this code... |
| 5 | `MODIFIER_VALUE_CD` | DOUBLE | NOT NULL |  | The value of the modification. Code set depends on the value of modifier_cd. |
| 6 | `MODIFIER_VALUE_FT` | DOUBLE |  |  | not used anymore. |
| 7 | `MODIFIER_VALUE_PERSON_ID` | DOUBLE | NOT NULL | FK→ | If the modification value is a person, the person_id will go in this field, and modifier_value_cd will be set to zero. |
| 8 | `MODIFIER_VAL_FT` | VARCHAR(100) |  |  | If the modification value is free text, the value will go in this field, and modifier_value_cd will be set to zero. |
| 9 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 10 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 11 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 12 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 13 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 14 | `VALID_FROM_DT_TM` | DATETIME | NOT NULL |  | Contains the Beginning Point of when a row in the table is valid. |
| 15 | `VALID_UNTIL_DT_TM` | DATETIME | NOT NULL |  | Contains the End Point of when a row in the table is valid. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `MODIFIER_VALUE_PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

