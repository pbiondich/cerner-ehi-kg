# RX_MED_ORD_DETAIL

> For an item, facility, age range combination, contains a row for each order entry detail that options are defined for.

**Description:** Pharmacy Medical Order Detail  
**Table type:** REFERENCE  
**Primary key:** `RX_MED_ORD_DETAIL_ID`  
**Columns:** 11  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility that options are defined for. |
| 2 | `ITEM_ID` | DOUBLE | NOT NULL | FK→ | The item that options are provided for. |
| 3 | `OE_FIELD_MEANING_ID` | DOUBLE | NOT NULL | FK→ | The order entry field that options are defined for. |
| 4 | `RESTRICT_IND` | DOUBLE | NOT NULL |  | Indicates if the value stored on the row is to be a restriction to the order entry application. |
| 5 | `RX_AGE_RANGE_ID` | DOUBLE | NOT NULL | FK→ | The age range that options are being created for. |
| 6 | `RX_MED_ORD_DETAIL_ID` | DOUBLE | NOT NULL | PK | Unique generated number that identifies a single row on the RX_MED_ORD_DETAIL table. |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `OE_FIELD_MEANING_ID` | [OE_FIELD_MEANING](OE_FIELD_MEANING.md) | `OE_FIELD_MEANING_ID` |
| `RX_AGE_RANGE_ID` | [RX_AGE_RANGE](RX_AGE_RANGE.md) | `RX_AGE_RANGE_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RX_MED_ORD_DETAIL_OPT](RX_MED_ORD_DETAIL_OPT.md) | `RX_MED_ORD_DETAIL_ID` |

