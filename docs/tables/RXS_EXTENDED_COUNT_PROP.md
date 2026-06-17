# RXS_EXTENDED_COUNT_PROP

> Contains additional information on when a count should be performed for a given location/item.

**Description:** RxStation Extended Count Property  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 11

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COUNTBACK_FLAG` | DOUBLE | NOT NULL |  | Flag used to determine if this item/location requires a physical count once the icurrent quantity level reached dynamic count level. |
| 2 | `COUNT_CONTROL_NBR` | DOUBLE | NOT NULL |  | A number indicating how often or when to start counting. |
| 3 | `COUNT_RULE_CD` | DOUBLE | NOT NULL |  | The count rule that is defined for this location/item. |
| 4 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item this count relates to. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location this count relates to. |
| 6 | `RXS_EXTENDED_COUNT_PROP_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the RXS_EXTENDED_COUNT_PROP table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |

