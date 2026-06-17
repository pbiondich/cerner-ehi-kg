# MM_DISCREPANCY

> Stores discrepencies between system calculated quantity on hand values and actual counts.

**Description:** Materials Management Discrepancy  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 22

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CLUSTER_CD` | DOUBLE | NOT NULL | FK→ | Cluster where the discrepancy was logged. |
| 2 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time the discrepancy was generated. |
| 3 | `CREATE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with CREATE_DT_TM. |
| 4 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | Facility where the discrepancy was logged. |
| 5 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | Location where the discrepancy was logged. |
| 6 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | Locator where the discrepancy was logged. |
| 7 | `MM_DISCREPANCY_ID` | DOUBLE | NOT NULL |  | Unique, generated number that identifies a single row on the MM_DISCREPANCY table. |
| 8 | `RESOLVED_COMMENT_TEXT_ID` | DOUBLE | NOT NULL | FK→ | Textual explanation of the resolution. May be 0. |
| 9 | `RESOLVED_DT_TM` | DATETIME |  |  | Date and time the discrepancy was resolved. |
| 10 | `RESOLVED_PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | Identifier of the inventory transaction line, item countback, or physical countback which was identified during resolution as causing the discrepancy. |
| 11 | `RESOLVED_PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | RESOLVED_PARENT_ENTITY_IDs associated table. |
| 12 | `RESOLVED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel documenting the resolution of the discrepancy. |
| 13 | `RESOLVED_REASON_CD` | DOUBLE | NOT NULL |  | The reason identified that caused the discrepancy. |
| 14 | `RESOLVED_TZ` | DOUBLE | NOT NULL |  | The time zone associated with RESOLVED_DT_TM. |
| 15 | `RXS_ITEM_COUNTBACK_ID` | DOUBLE | NOT NULL | FK→ | The countback that had a discrepancy. |
| 16 | `STATUS_CD` | DOUBLE | NOT NULL |  | The status of the discrepancy. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WITNESS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The Personnel that witnessed the documentation of the resolution of the discrepancy. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLUSTER_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RESOLVED_COMMENT_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `RESOLVED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RXS_ITEM_COUNTBACK_ID` | [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `RXS_ITEM_COUNTBACK_ID` |
| `WITNESS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

