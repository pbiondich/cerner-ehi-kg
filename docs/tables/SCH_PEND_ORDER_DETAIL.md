# SCH_PEND_ORDER_DETAIL

> Contains order detail information about an appointment which will be created.

**Description:** Scheduling Pending Order Detail  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `OE_FIELD_DISPLAY_VALUE` | VARCHAR(255) |  |  | The detail display value associated to the pending order. |
| 2 | `OE_FIELD_DT_TM_VALUE` | DATETIME |  |  | The detail display value associated to the pending order. |
| 3 | `OE_FIELD_ID` | DOUBLE | NOT NULL | FK→ | The field identifier associated to the pending order. |
| 4 | `OE_FIELD_MEANING` | VARCHAR(25) |  |  | The field meaning associated to the pending order. |
| 5 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL | FK→ | The field meaning identifier associated to the pending order. |
| 6 | `OE_FIELD_VALUE` | DOUBLE |  |  | The detail value associated to the pending order. |
| 7 | `SCH_PEND_ORDER_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the SCH_PEND_ORDER_DETAIL table. |
| 8 | `SCH_PEND_ORDER_ID` | DOUBLE | NOT NULL | FK→ | The pending order identifier. |
| 9 | `SEQ_NBR` | DOUBLE | NOT NULL |  | The sequence in which the detail should be used when multiple values exist for a specific field identifier. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OE_FIELD_ID` | [ORDER_ENTRY_FIELDS](ORDER_ENTRY_FIELDS.md) | `OE_FIELD_ID` |
| `OE_FIELD_MEANING_ID` | [OE_FIELD_MEANING](OE_FIELD_MEANING.md) | `OE_FIELD_MEANING_ID` |
| `SCH_PEND_ORDER_ID` | [SCH_PEND_ORDER](SCH_PEND_ORDER.md) | `SCH_PEND_ORDER_ID` |

