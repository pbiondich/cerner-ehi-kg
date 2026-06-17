# RXS_ALERT

> This table represents an alert that has been generated against an RxStation device.

**Description:** RxStation Alert  
**Table type:** ACTIVITY  
**Primary key:** `RXS_ALERT_ID`  
**Columns:** 20  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CREATE_DT_TM` | DATETIME |  |  | The date/time this row was inserted. |
| 2 | `CREATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel responsible for this row being inserted. |
| 3 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | The dispense event this alert was generated for. |
| 4 | `INV_ITEM_ID` | DOUBLE | NOT NULL | FK→ | Foreign key to ITEM_DEFINITION. Indicates the item to track inventory on. |
| 5 | `LOCATOR_CD` | DOUBLE | NOT NULL | FK→ | The compartment in the device that is related to this alert. |
| 6 | `OWNER_FACILITY_CD` | DOUBLE | NOT NULL | FK→ | The facility that is responsible for the RxStation device. |
| 7 | `RXS_ALERT_ID` | DOUBLE | NOT NULL | PK | Generated unique identifier for each row in this table. |
| 8 | `RXS_CLSTR_CD` | DOUBLE | NOT NULL |  | The cluster (grouping) that the RxStation device belongs to. |
| 9 | `RXS_DEVICE_LOC_CD` | DOUBLE | NOT NULL |  | The representation of the device in the Location model. PharmNet and Supply Chain both require this for dispensing and inventory tracking. |
| 10 | `RXS_DEVICE_SR_CD` | DOUBLE | NOT NULL | FK→ | The representation of the device in the Service Resource model. PharmNet requires this for dispensing routing. |
| 11 | `STATE_CD` | DOUBLE | NOT NULL |  | indicates the state (status) that the alert is currently in. This is a required field. |
| 12 | `STATE_DT_TM` | DATETIME |  |  | The date/time of the last state change. |
| 13 | `STATE_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The personnel responsible for the change in state. |
| 14 | `SVRTY_CD` | DOUBLE | NOT NULL |  | Indicates the severity of this alert. |
| 15 | `TYPE_CD` | DOUBLE | NOT NULL |  | Indicates the type of alert. This is a required field. |
| 16 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 17 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 18 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 19 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 20 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CREATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `INV_ITEM_ID` | [ITEM_DEFINITION](ITEM_DEFINITION.md) | `ITEM_ID` |
| `LOCATOR_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `OWNER_FACILITY_CD` | [LOCATION](LOCATION.md) | `LOCATION_CD` |
| `RXS_DEVICE_SR_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `STATE_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [RXS_ALERT_AUDIT_HX](RXS_ALERT_AUDIT_HX.md) | `RXS_ALERT_ID` |
| [RXS_ALERT_LOC_RELTN](RXS_ALERT_LOC_RELTN.md) | `RXS_ALERT_ID` |
| [RXS_TASK_ALERT_RELTN](RXS_TASK_ALERT_RELTN.md) | `RXS_ALERT_ID` |

