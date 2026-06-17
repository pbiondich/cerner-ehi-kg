# SA_FLUID_ADMIN

> Contains records that document the administration of fluids in an anesthesia record Based on the number of administrations of a given fluid. Estimate 1:1 with SA_FLUID. 130,500

**Description:** SA Fluid Admin  
**Table type:** ACTIVITY  
**Primary key:** `SA_FLUID_ADMIN_ID`  
**Columns:** 50  
**Referenced by:** 3 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE | NOT NULL |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME | NOT NULL |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADMIN_AMOUNT` | DOUBLE |  |  | The amount of the fluid administered |
| 6 | `ADMIN_DOSAGE` | DOUBLE |  |  | This column is not being used. OBSOLETE |
| 7 | `ADMIN_RATE_CD` | DOUBLE | NOT NULL |  | ADMIN RATE CODE |
| 8 | `ADMIN_ROUTE_CD` | DOUBLE | NOT NULL |  | The route used for the administration |
| 9 | `ADMIN_SITE_CD` | DOUBLE | NOT NULL |  | The site that the fluid was administered |
| 10 | `ADMIN_START_DT_TM` | DATETIME |  |  | This column is not being used. OBSOLETE |
| 11 | `ADMIN_STOP_DT_TM` | DATETIME |  |  | This column is not being used. OBSOLETE |
| 12 | `AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit of measure for the amount of the fluid administered |
| 13 | `BEGIN_BAG_EVENT_ID` | DOUBLE | NOT NULL |  | The event ID for the last begin bag written out by SAAnesthesia (from CLINICAL EVENT) |
| 14 | `CHARGED_IND` | DOUBLE | NOT NULL |  | Indicates whether admin has been charged for from anesthesia |
| 15 | `CONTINUED_NO_BEGIN_BAG_IND` | DOUBLE | NOT NULL |  | Indicates the fluid was continued from an order which didn't have a begin bag event. |
| 16 | `CONTINUE_OUT_IND` | DOUBLE | NOT NULL |  | An indicator to Continue Fluid Admin Orders Out |
| 17 | `DDMO_IND` | DOUBLE | NOT NULL |  | Indicates whether the admin sent through the DDMO server when finalized |
| 18 | `DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | This column is not being used. OBSOLETE |
| 19 | `EVENT_ID` | DOUBLE | NOT NULL |  | Uniquely identifies a logical clinical event row. It is returned from DDMO. It is used to cancel a med order and result when unfinalizing a record.. |
| 20 | `FLUID_ADMIN_TYPE_FLAG` | DOUBLE | NOT NULL |  | Type of Fluid Administration. FLUID_ADMIN_TYPE_BOLUS = 1, FLUID_ADMIN_TYPE_INFUSION = 2. |
| 21 | `GROUP_EVENT_ID` | DOUBLE | NOT NULL |  | identifier of fluid administration's grouper clinical event (CLINICAL_EVENT.EVENT_ID) |
| 22 | `HEIGHT` | DOUBLE |  |  | Height value |
| 23 | `HEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | HEIGHT UNIT CODE |
| 24 | `IO_EVENT_ID` | DOUBLE | NOT NULL |  | identifier of fluid administration's intake or output result clinical event(CLINICAL_EVENT.EVENT_ID) |
| 25 | `LONG_TEXT_ID` | DOUBLE | NOT NULL |  | The long_text record that contains the comment for the administration |
| 26 | `ORDERED_IND` | DOUBLE | NOT NULL |  | Indicates whether the admin was documented against an existing order or is an ad hoc admin |
| 27 | `ORDER_ID` | DOUBLE | NOT NULL |  | Order that the admin is associated to |
| 28 | `ORDER_LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | The LONG_TEXT record that contains the comment for the order |
| 29 | `PREVIOUS_FLUID_ADMIN_ID` | DOUBLE | NOT NULL | FK→ | The id to the admin record before the record was changed. If 0, this is the original unchanged record |
| 30 | `PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The user who documented the administration, if 0, added by a macro |
| 31 | `RESULT_SET_ID` | DOUBLE | NOT NULL |  | Identifier of the Result Set the Fluid Administrations intake or output result belongs to. From CE_RESULT_SET_LINK. |
| 32 | `SA_FLUID_ADMIN_ID` | DOUBLE | NOT NULL | PK | Unique value that identifies the medication administration record |
| 33 | `SA_FLUID_ID` | DOUBLE | NOT NULL | FK→ | The SA_FLUID record id that this administration record is documenting |
| 34 | `SA_MACRO_ID` | DOUBLE | NOT NULL | FK→ | Ties to the macro that added the admin to the anesthesia record, if 0, added by user |
| 35 | `SENT_DT_TM` | DATETIME |  |  | Date/Time when administration was sent to Clinical Event |
| 36 | `TASK_ID` | DOUBLE | NOT NULL | FK→ | Task that the admin is associated to |
| 37 | `TEMPLATE_ORDER_ID` | DOUBLE | NOT NULL | FK→ | Parent Order that admin is documented against |
| 38 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 39 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 40 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 41 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 42 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 43 | `VOLUME_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of volume |
| 44 | `VOLUME_RATE_AMOUNT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for amount field of Volume Rate |
| 45 | `VOLUME_RATE_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time field of Volume Rate |
| 46 | `WBD_DOSAGE_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for dosage in WBD |
| 47 | `WBD_TIME_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for time in WBD |
| 48 | `WBD_WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | Default unit for weight in WBD |
| 49 | `WEIGHT` | DOUBLE |  |  | Weight Value |
| 50 | `WEIGHT_UNIT_CD` | DOUBLE | NOT NULL |  | The unit code for Weight |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ORDER_LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |
| `PREVIOUS_FLUID_ADMIN_ID` | [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `SA_FLUID_ADMIN_ID` |
| `PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SA_FLUID_ID` | [SA_FLUID](SA_FLUID.md) | `SA_FLUID_ID` |
| `SA_MACRO_ID` | [SA_MACRO](SA_MACRO.md) | `SA_MACRO_ID` |
| `TASK_ID` | [TASK_ACTIVITY](TASK_ACTIVITY.md) | `TASK_ID` |
| `TEMPLATE_ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |

## Referenced by (3)

| From table | Column |
|------------|--------|
| [SA_FLUID_ADMIN](SA_FLUID_ADMIN.md) | `PREVIOUS_FLUID_ADMIN_ID` |
| [SA_FLUID_ADMIN_BAG](SA_FLUID_ADMIN_BAG.md) | `SA_FLUID_ADMIN_ID` |
| [SA_FLUID_ADMIN_ITEM](SA_FLUID_ADMIN_ITEM.md) | `SA_FLUID_ADMIN_ID` |

