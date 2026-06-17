# RXS_LOCATION_TASK

> Represents tasks that have been generated for a location.

**Description:** RxStation Location Task  
**Table type:** ACTIVITY  
**Primary key:** `RXS_LOCATION_TASK_ID`  
**Columns:** 48  
**Referenced by:** 7 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTUAL_QTY` | DOUBLE | NOT NULL |  | Actual quantity used to complete this task. For example, the requested quantity may call for 50 units of an item, but the pharmacy only contains 40 of this item. |
| 2 | `CAPACITY_ATTR_CONFIG_NBR` | DOUBLE |  |  | The capacity configuration relevant to this specific task. |
| 3 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The catalog code for an item for which a task is created in rxs_location_task. |
| 4 | `CLUSTER_CD` | DOUBLE | NOT NULL | FK→ | If the location_cd is an RxStation device, this is the cluster (grouping) that the RxStation device belongs to. |
| 5 | `CONNECTORS_ATTR_CONFIG_NBR` | DOUBLE |  |  | The connectors configuration relevant to this specific task. |
| 6 | `CREATE_DT_TM` | DATETIME | NOT NULL |  | Date and time the task was created. |
| 7 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel who created this task. |
| 8 | `CREATE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with CREATE_DT_TM. |
| 9 | `ENCNTR_ID` | DOUBLE |  | FK→ | Refers to a patient encounter which is associated to a location task. Can be 0. (skewed column, most of them will be 0). As of today, we will use that field if we do not have SurgiNet integration. |
| 10 | `EXPIRE_DT_TM` | DATETIME |  |  | Planned expiration date for items used on a replenishment task. |
| 11 | `EXPIRE_TZ` | DOUBLE | NOT NULL |  | Time zone associated with EXPIRE_DT_TM. |
| 12 | `FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility that is responsible for this location. |
| 13 | `FILL_LOCATION_CD` | DOUBLE | NOT NULL | FK→ | For replenishment tasks, this is the location from which the item is expected to be pulled. |
| 14 | `FILL_WITNESS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | If a witness is required to check the fill for the transfer in the pharmacy, this is the personnel ID of the person who checked the fill. |
| 15 | `INV_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Indicates the item this task pertains to. |
| 16 | `LINKED_TASK_ID` | DOUBLE | NOT NULL |  | *** obsolete *** |
| 17 | `LOCATION_CD` | DOUBLE | NOT NULL | FK→ | The location that this task pertains to. |
| 18 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | The lowest level of the location hierarchy for which the item will be placed. |
| 19 | `MED_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Indicates the pharmacy formulary item for this task. |
| 20 | `ORDER_ACTION_SEQ` | DOUBLE | NOT NULL |  | The action sequence at the time of task for tasks with an order_id context. |
| 21 | `ORDER_ID` | DOUBLE |  | FK→ | The order that was satisfied by this task. |
| 22 | `PACKAGE_TYPE_DESC_TXT` | VARCHAR(100) | NOT NULL |  | Description of the type of package for the item on the task. |
| 23 | `PACKAGE_TYPE_ID` | DOUBLE | NOT NULL | FK→ | Indicates the package (unit of measure) for the item. Examples include tablets, bottles, etc. |
| 24 | `PACKAGE_TYPE_QTY` | DOUBLE | NOT NULL |  | The quantity of base packages contained in this package. For example, if this item comes packed individually, a box might contain multiple individual packages. |
| 25 | `PACKAGE_TYPE_UOM_CD` | DOUBLE | NOT NULL |  | Unit of measure for the package. |
| 26 | `PHARM_TYPE_CD` | DOUBLE | NOT NULL |  | Pharmacy type code that indicates if the task applies to Inpatient or Retail. |
| 27 | `RECONCILE_FLAG` | DOUBLE | NOT NULL |  | Indicates whether the transfer has been reconciled. Used for transfers to a provider. Values include 0 = reconciliation not needed; 1 = needs reconciliation; 2 = reconciliation in process; 3 = reconciliation complete. |
| 28 | `REQUESTED_QTY` | DOUBLE | NOT NULL |  | Quantity requested for this task. For example, in a replenishment task, this is the quantity of the item needed to completely fill the locator as determined by the system during the TBR (task-based replenishment) process. |
| 29 | `RXS_ALERT_ID` | DOUBLE | NOT NULL |  | *** OBSOLETE *** |
| 30 | `RXS_ITEM_GROUP_ACT_ID` | DOUBLE | NOT NULL | FK→ | Macro table's index id. This is used to match the rxs_item_group_act table's macro info. |
| 31 | `RXS_LOCATION_TASK_ID` | DOUBLE | NOT NULL | PK | Unique, generated number that identifies a single row on the RXS_LOCATION_TASK table. |
| 32 | `RXS_RECEIVING_DETAIL_ID` | DOUBLE | NOT NULL | FK→ | Documents the forms used for this receiving drug task. |
| 33 | `RXS_WORKLIST_EVENT_ID` | DOUBLE | NOT NULL | FK→ | The worklist event that generated this task. |
| 34 | `SA_TODO_LIST_PROCESSED_IND` | DOUBLE | NOT NULL |  | indicate if surginet anesthesia has retrieved the activity for the to do list. |
| 35 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL | FK→ | The representation of the location in the service resource model. |
| 36 | `STATUS_DT_TM` | DATETIME |  |  | The date and time the task_status_cd field was last updated. |
| 37 | `STATUS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel that last updated the task_status_cd field. |
| 38 | `STATUS_TZ` | DOUBLE | NOT NULL |  | Time zone associated with STATUS_DT_TM. |
| 39 | `SURG_CASE_ID` | DOUBLE |  | FK→ | Refers to a surgery case which is associated to a location task. Can be 0 (skewed column, most of them will be 0). Location tasks that are created for anesthesia cart dispenses, returns and wastes will be associated with a surgical case, if SurgiNet integration exists. |
| 40 | `TASK_STATUS_CD` | DOUBLE | NOT NULL |  | The task's current status. For example: Pending, In Process. |
| 41 | `TASK_TYPE_CD` | DOUBLE | NOT NULL |  | The type of task - for example: replenish, load, unload. |
| 42 | `TRANSFER_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | Personnel who received the medication and is responsible for the transfer between the fill_location_cd and the location_cd. |
| 43 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 44 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 45 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 46 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 47 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 48 | `WITNESS_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel that was responsible for witnessing this task. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CLUSTER_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FILL_LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `FILL_WITNESS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `INV_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOCATION_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `MED_ITEM_ID` | [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `ITEM_ID` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `PACKAGE_TYPE_ID` | [PACKAGE_TYPE](PACKAGE_TYPE.md) | `PACKAGE_TYPE_ID` |
| `RXS_ITEM_GROUP_ACT_ID` | [RXS_ITEM_GROUP_ACT](RXS_ITEM_GROUP_ACT.md) | `RXS_ITEM_GROUP_ACT_ID` |
| `RXS_RECEIVING_DETAIL_ID` | [RXS_RECEIVING_DETAIL](RXS_RECEIVING_DETAIL.md) | `RXS_RECEIVING_DETAIL_ID` |
| `RXS_WORKLIST_EVENT_ID` | [RXS_WORKLIST_EVENT](RXS_WORKLIST_EVENT.md) | `RXS_WORKLIST_EVENT_ID` |
| `SERVICE_RESOURCE_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `STATUS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |
| `TRANSFER_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `WITNESS_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (7)

| From table | Column |
|------------|--------|
| [RXS_ACTIVITY_INDEX](RXS_ACTIVITY_INDEX.md) | `RXS_LOCATION_TASK_ID` |
| [RXS_ITEM_COUNTBACK](RXS_ITEM_COUNTBACK.md) | `RXS_LOCATION_TASK_ID` |
| [RXS_LOCATION_TASK_RELTN](RXS_LOCATION_TASK_RELTN.md) | `CHILD_TASK_ID` |
| [RXS_LOCATION_TASK_RELTN](RXS_LOCATION_TASK_RELTN.md) | `PARENT_TASK_ID` |
| [RXS_TASK_ALERT_RELTN](RXS_TASK_ALERT_RELTN.md) | `RXS_LOCATION_TASK_ID` |
| [RXS_TASK_DISPENSE_RELTN](RXS_TASK_DISPENSE_RELTN.md) | `RXS_LOCATION_TASK_ID` |
| [RXS_TASK_SR_HX](RXS_TASK_SR_HX.md) | `RXS_LOCATION_TASK_ID` |

