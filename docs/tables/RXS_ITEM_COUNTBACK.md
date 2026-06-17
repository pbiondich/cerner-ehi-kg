# RXS_ITEM_COUNTBACK

> Shows the actual and anticipated counts every time a countback is required by the system.

**Description:** RxStation Item Countback  
**Table type:** ACTIVITY  
**Primary key:** `RXS_ITEM_COUNTBACK_ID`  
**Columns:** 30  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_QTY` | DOUBLE | NOT NULL |  | The actual physical quantity found on hand during a countback. |
| 2 | `CLUSTER_CD` | DOUBLE | NOT NULL | FK→ | If the location_cd is an RxStation device, this is the cluster (grouping) that the RxStation device belongs to. |
| 3 | `COUNTBACK_SEQ` | DOUBLE | NOT NULL |  | Sequence number differentiating multiple countback attempts during the same encounter with the same location for the same item. |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | Date this countback was performed. |
| 5 | `CREATE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with CREATE_DT_TM. |
| 6 | `EVENT_TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of event that was being processed when the countback took place. |
| 7 | `EXPECTED_QTY` | DOUBLE | NOT NULL |  | The quantity that the device had stored in its inventory at the time of the countback according to the system. |
| 8 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility where the countback was performed. |
| 9 | `INV_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Indicates the item this countback was for. |
| 10 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location where the countback was performed. PharmNet and Supply Chain both require this for dispensing and inventory tracking. |
| 11 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | The bin or tray in an RxStation device where the item countback was done. |
| 12 | `MED_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Indicates the pharmacy formulary item for this task. |
| 13 | `MED_PRODUCT_ID` | DOUBLE | NOT NULL | FK→ | The id that identifies the actual pharmacy product item that is being counted. |
| 14 | `PACKAGE_TYPE_DESC_TXT` | VARCHAR(100) | NOT NULL |  | Description of the package type of the item being counted. |
| 15 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | The package type of the item being counted. |
| 16 | `PACKAGE_TYPE_QTY` | DOUBLE | NOT NULL |  | The quantity in the package type of the item being counted. |
| 17 | `PACKAGE_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | The unit of measure for the package for the item being counted. |
| 18 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type code that indicates if the countback occurred at an Inpatient or Retail establishment. |
| 19 | `PROD_DISPENSE_HX_ID` | DOUBLE | NOT NULL |  | Product dispense history information for the dispense event during which the countback took place. |
| 20 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel performing the countback. |
| 21 | `RXS_ITEM_COUNTBACK_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RXS_ITEM_COUNTBACK table. |
| 22 | `RXS_LOCATION_TASK_ID` | DOUBLE | NOT NULL | FK→ | The task that triggered the countback to occur. |
| 23 | `RX_WORKFLOW_STS_ID` | DOUBLE | NOT NULL | FK→ | The workflow step during which the countback took place. |
| 24 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The representation in the service resource model of the location where the countback was performed. PharmNet requires this for dispensing routing. |
| 25 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 26 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 27 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 28 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 29 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 30 | `WITNS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Identifier for witness overseeing countback event |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLUSTER_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `INV_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `MED_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `MED_PRODUCT_ID` | [MED_PRODUCT](MED_PRODUCT.md) | `MED_PRODUCT_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `RXS_LOCATION_TASK_ID` | [RXS_LOCATION_TASK](RXS_LOCATION_TASK.md) | `RXS_LOCATION_TASK_ID` |
| `RX_WORKFLOW_STS_ID` | [RX_WORKFLOW_STS](RX_WORKFLOW_STS.md) | `RX_WORKFLOW_STS_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `WITNS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [MM_DISCREPANCY](MM_DISCREPANCY.md) | `RXS_ITEM_COUNTBACK_ID` |

