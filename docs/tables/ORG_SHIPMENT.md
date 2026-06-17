# ORG_SHIPMENT

> Contains organization preferences for the BB Shipping & Transfer application

**Description:** Organization Shipment Table  
**Table type:** REFERENCE  
**Primary key:** `ORG_SHIPMENT_ID`  
**Columns:** 18  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACCEPT_EXPIRED_PROD_IND` | DOUBLE | NOT NULL |  | Indicates whether or not an organization will allow receiving expired products which are shipped. |
| 2 | `ACCEPT_POS_RESULT_IND` | DOUBLE | NOT NULL |  | Indicates whether or not an organization will allow receiving products with positive results which are shipped. |
| 3 | `ACCEPT_QUARANTINED_PROD_IND` | DOUBLE | NOT NULL |  | Indicates whether or not an organization will allow receiving quarantined products which are shipped. |
| 4 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 5 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 6 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 7 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 8 | `DESTROY_ONCE_EXPIRED_IND` | DOUBLE | NOT NULL |  | Indicates whether or not the shipping organization will destroy a product once it has been shipped and is expired. |
| 9 | `INVENTORY_AREA_CD` | DOUBLE | NOT NULL | FK→ | Indicates the inventory area to which the preferenced belong. |
| 10 | `ORGANIZATION_ID` | DOUBLE | NOT NULL | FK→ | Indicates the organization to which the preferenced belong. |
| 11 | `ORG_SHIPMENT_ID` | DOUBLE | NOT NULL | PK | The unique identifier for the ORG_SHIPMENT table. |
| 12 | `OWNER_AREA_CD` | DOUBLE | NOT NULL | FK→ | Indicates the owner area to which the preferenced belong. |
| 13 | `REQ_TESTING_COMPLETE_IND` | DOUBLE | NOT NULL |  | Indicates whether or not an organization will allow receiving products whose testing is not complete. |
| 14 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 15 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 16 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 17 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 18 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `INVENTORY_AREA_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `ORGANIZATION_ID` | [ORGANIZATION](ORGANIZATION.md) | `ORGANIZATION_ID` |
| `OWNER_AREA_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [ACCEPT_QUAR_REASON](ACCEPT_QUAR_REASON.md) | `ORG_SHIPMENT_ID` |

