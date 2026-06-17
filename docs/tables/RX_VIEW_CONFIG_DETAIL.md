# RX_VIEW_CONFIG_DETAIL

> Contains information around each filter associated with a view

**Description:** Pharmacy View Configuration Detail  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 14

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CONFIG_DETAIL_MEAN` | VARCHAR(32) | NOT NULL |  | Based the detail_type_cd, the meaning will be a unique string representing the specific configuration detail. It is not required for all configuration details. |
| 2 | `CONFIG_DETAIL_SEQ` | DOUBLE | NOT NULL |  | Based on the detail_type_cd, the sequence will represent the order of the configuration details for that detail type. It is not required for all configuration details. |
| 3 | `CONFIG_DETAIL_SORT_FLAG` | DOUBLE |  |  | Based on detail_type_cd, the indicator will represent the sort direction for the specific configuration detail. It is required for the configuration detail that is used for sorting |
| 4 | `DETAIL_TYPE_CD` | DOUBLE | NOT NULL |  | The type of filter this row is defining. |
| 5 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility that is associated with the view. |
| 6 | `PARENT_ENTITY_ID` | DOUBLE | NOT NULL |  | ID of the detail type that is updated on this row |
| 7 | `PARENT_ENTITY_NAME` | VARCHAR(32) | NOT NULL |  | The detail type that is updated on this row. |
| 8 | `RX_VIEW_CONFIG_DETAIL_ID` | DOUBLE | NOT NULL |  | Unique generated number that identifies a single row on the RX_VIEW_CONFIG_DETAIL table. |
| 9 | `RX_VIEW_CONFIG_ID` | DOUBLE | NOT NULL | FK→ | The header information for this pharmacy view. |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RX_VIEW_CONFIG_ID` | [RX_VIEW_CONFIG](RX_VIEW_CONFIG.md) | `RX_VIEW_CONFIG_ID` |

