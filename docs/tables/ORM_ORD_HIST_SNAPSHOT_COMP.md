# ORM_ORD_HIST_SNAPSHOT_COMP

> Contains history snapshot components. These components are the individual orders which are in the snapshots

**Description:** orm_order_history_snapshot_component  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 24

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQUENCE` | DOUBLE | NOT NULL | FK→ | The order action sequence of the order when the snapshot was taken. |
| 2 | `ACTIVITY_TYPE_CD` | DOUBLE | NOT NULL |  | The order's activity type. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | The catalog code of the order. |
| 4 | `CATALOG_TYPE_CD` | DOUBLE | NOT NULL |  | The catalog type of the order. |
| 5 | `CLINICAL_DISPLAY_LINE` | VARCHAR(255) |  |  | The order's clinical display line when the snapshot was taken. |
| 6 | `COMPLIANCE_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The compliance long text id. |
| 7 | `COMPLIANCE_STATUS_CD` | DOUBLE | NOT NULL |  | The order's compliance status when the snapshot was taken. |
| 8 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | The encounter for which the medication history snapshot was taken |
| 9 | `HNA_ORDER_MNEMONIC` | VARCHAR(100) |  |  | Order HNA mnemonic. |
| 10 | `ORDERED_AS_MNEMONIC` | VARCHAR(100) |  |  | Ordered as mnemonic. |
| 11 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | The order's id. |
| 12 | `ORDER_LAST_UPD_DT_TM` | DATETIME |  |  | The date the order was last updated at the time that the snapshot was taken. |
| 13 | `ORDER_LAST_UPD_TZ` | DOUBLE |  |  | The time zone for the last updated date/time. |
| 14 | `ORDER_MNEMONIC` | VARCHAR(100) |  |  | Order mnemonic. |
| 15 | `ORDER_STATUS_CD` | DOUBLE | NOT NULL |  | The order's status. |
| 16 | `ORM_ORD_HIST_SNAPSHOT_COMP_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the orm_ord_hist_snapshot_comp table. |
| 17 | `SIMPLIFIED_DISPLAY_LINE` | VARCHAR(1000) |  |  | The order's simplified display line when the snapshot was taken. |
| 18 | `SNAPSHOT_ID` | DOUBLE | NOT NULL | FK→ | The snapshot component is linked to this snapshot. |
| 19 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 20 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 21 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 22 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 23 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 24 | `VENUE_TYPE_CD` | DOUBLE | NOT NULL |  | The venue type of the order at the time the snapshot was created. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ACTION_SEQUENCE` | [ORDER_ACTION](ORDER_ACTION.md) | `ACTION_SEQUENCE` |
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `COMPLIANCE_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `ORDER_ID` | [ORDER_ACTION](ORDER_ACTION.md) | `ORDER_ID` |
| `SNAPSHOT_ID` | [ORM_ORD_HIST_SNAPSHOT](ORM_ORD_HIST_SNAPSHOT.md) | `ORM_ORD_HIST_SNAPSHOT_ID` |

