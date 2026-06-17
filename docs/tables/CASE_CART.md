# CASE_CART

> This table contains case cart information for a surgical case.

**Description:** Case Cart  
**Table type:** ACTIVITY  
**Primary key:** `CASE_CART_ID`  
**Columns:** 30  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `CASE_CART_ID` | DOUBLE | NOT NULL | PK | The primary key, uniquely identifying a row on this table |
| 6 | `COMMENT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 7 | `CREATE_APPLCTX` | DOUBLE |  |  | The application context responsible for inserting this row on the table |
| 8 | `CREATE_DT_TM` | DATETIME |  |  | The date and time this row was inserted |
| 9 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL |  | The person responsible for inserting this row on the table |
| 10 | `CREATE_TASK` | DOUBLE |  |  | The task responsible for inserting this row on the table |
| 11 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type that this case cart is associated with. |
| 12 | `FINALIZE_DT_TM` | DATETIME |  |  | The date and time the case cart was finalized |
| 13 | `LOCKED_APPLCTX` | DOUBLE |  |  | The application context locking the record |
| 14 | `MODIFIED_IND` | DOUBLE |  |  | An indicator of whether or not this case cart has been modified, i.e. requested quantity changed, item added or deleted |
| 15 | `PREF_CARD_TYPE_FLAG` | DOUBLE |  |  | *** OBSOLETE *** |
| 16 | `PRINT_DT_TM` | DATETIME |  |  | *** OBSOLETE *** |
| 17 | `REQUISITION_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 18 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this case cart |
| 19 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | The surgical case associated with this case cart |
| 20 | `TOT_EQUIP_COST_AVG` | DOUBLE |  |  | The total equipment cost (average cost) of all equipment items associated with this case cart. |
| 21 | `TOT_EQUIP_COST_LAST` | DOUBLE |  |  | The total equipment cost (last cost) of all equipment items associated with this case pick list. |
| 22 | `TOT_SUPPLY_COST_AVG` | DOUBLE |  |  | The total supply cost (average cost) of all supply items associated with this case pick list. |
| 23 | `TOT_SUPPLY_COST_LAST` | DOUBLE |  |  | The total supply cost (last cost) of all supply items associated with this case pick list. |
| 24 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 25 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 26 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 27 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 28 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 29 | `VERIFIED_BY_ID` | DOUBLE | NOT NULL | FK→ | The person responsible for verifying this case cart |
| 30 | `VERIFIED_DT_TM` | DATETIME |  |  | The date and time this case cart pick list was verified |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |
| `VERIFIED_BY_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [CASE_CART_PICK_LIST](CASE_CART_PICK_LIST.md) | `CASE_CART_ID` |

