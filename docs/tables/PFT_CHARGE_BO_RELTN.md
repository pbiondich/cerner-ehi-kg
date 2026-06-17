# PFT_CHARGE_BO_RELTN

> Identifies a charge(pft_charge_id) as being a member of the charge group identified by benefit_order_id, including any billing information that is specific to this relationship (such as the health plan coverage of the charge for the coordination of benefits represented by the charge group).

**Description:** ProFit Charge Benefit Order Relation  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 21

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `ADJUDICATED_STATUS_CD` | DOUBLE | NOT NULL |  | Status of adjudication for the charge |
| 6 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 7 | `BENEFIT_ORDER_ID` | DOUBLE | NOT NULL | FK→ | FK to the benefit_order table |
| 8 | `BILL_TEMPL_ID` | DOUBLE | NOT NULL | FK→ | FK to the bill_templ table |
| 9 | `BT_COND_RESULT_ID` | DOUBLE | NOT NULL |  | FK to the bt_cond_result table as of iteration 2.2 no longer used |
| 10 | `COVERED_BITMAP` | DOUBLE | NOT NULL |  | This column utilizes bit manipulation to determine whether a charge is covered by the associated health plan. |
| 11 | `COVERED_IND` | DOUBLE |  |  | Covered Indicator |
| 12 | `DENIED_IND` | DOUBLE |  |  | ** obsolete ** This column is no longer used. Denied Indicator |
| 13 | `DENIED_REASON_CD` | DOUBLE | NOT NULL |  | ** obsolete ** This column is no longer used. Denied Reason Code |
| 14 | `END_EFFECTIVE_DT_TM` | DATETIME |  |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 15 | `PFT_CHARGE_BO_RELTN_ID` | DOUBLE | NOT NULL |  | Primary Key |
| 16 | `PFT_CHARGE_ID` | DOUBLE | NOT NULL | FK→ | FK to the pft_charge table |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `BENEFIT_ORDER_ID` | [BENEFIT_ORDER](BENEFIT_ORDER.md) | `BENEFIT_ORDER_ID` |
| `BILL_TEMPL_ID` | [BILL_TEMPL](BILL_TEMPL.md) | `BILL_TEMPL_ID` |
| `PFT_CHARGE_ID` | [PFT_CHARGE](PFT_CHARGE.md) | `PFT_CHARGE_ID` |

