# RXA_WORK_LOAD_OBS_ST

> This table will store retail work load information

**Description:** RXA_WORK_LOAD_OBS_ST (Summary Table)  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 17

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTION_SEQ` | DOUBLE | NOT NULL |  | Action_Sequence from order_action table |
| 2 | `DISPENSE_HX_ID` | DOUBLE | NOT NULL | FK→ | Dispense_hx_id from Dispense_hx table |
| 3 | `DISPENSE_STATUS_HX_ID` | DOUBLE | NOT NULL | FK→ | Dispense_Status_hx_id from Dispense_Status_hx table |
| 4 | `DISP_FROM_SR_CD` | DOUBLE | NOT NULL | FK→ | Service_Resource_Cd from Service_Resource table |
| 5 | `ORDER_ID` | DOUBLE | NOT NULL | FK→ | Order_id from orders table |
| 6 | `RXA_LEVEL5_CD` | DOUBLE | NOT NULL |  | work station that requested the event |
| 7 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 8 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 9 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 10 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 11 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 12 | `WORK_DT_TM` | DATETIME |  |  | IF work_type is order_action, this date will be set to action_dt_tm (from pha_ord_act_obs_st table). If work_type is dispense_hx, this date will be set to disp_priority_dt_tm (from pha_disp_obs_st table) IF work_type is dispense tracking, this date will be set to completed_dt_tm (from dispense_status_hx table) |
| 13 | `WORK_DT_TZ` | DOUBLE | NOT NULL |  | Work time zone for work_dt_tm. For inpatient rows, this is the time zone of the encounter. For Retail Pharmacy, it is the time zone of the pharmacy's facility. |
| 14 | `WORK_LOAD_ID` | DOUBLE | NOT NULL |  | Unique number per Row. NOTE: Will use sequence PHA_RANGE_SEQ |
| 15 | `WORK_TYPE_CD` | DOUBLE | NOT NULL |  | If the type of work is an Order-Action, then it would come from codeset 6003 If type of work is a dispense event, then it would come from codeset 4032 If type of work is a dispense tracking step, then it would come from codeset 4502. |
| 16 | `WORK_TYPE_CS_FLAG` | DOUBLE | NOT NULL |  | Valid values are 6003, 4032, 4502 |
| 17 | `WORK_USER_ID` | DOUBLE | NOT NULL | FK→ | IF work_type is order_action, this field will be set to action_prsnl_id (from pha_ord_act_obs_st table). If work_type is dispense_hx, this field will be set to run_user_id (from pha_disp_obs_st table) IF work_type is dispense tracking, this field will be set to completed_user_id (from dispense_status_hx table) |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DISPENSE_HX_ID` | [DISPENSE_HX](DISPENSE_HX.md) | `DISPENSE_HX_ID` |
| `DISPENSE_STATUS_HX_ID` | [DISPENSE_STATUS_HX](DISPENSE_STATUS_HX.md) | `DISPENSE_STATUS_HX_ID` |
| `DISP_FROM_SR_CD` | [SERVICE_RESOURCE](SERVICE_RESOURCE.md) | `SERVICE_RESOURCE_CD` |
| `ORDER_ID` | [ORDERS](ORDERS.md) | `ORDER_ID` |
| `WORK_USER_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |

