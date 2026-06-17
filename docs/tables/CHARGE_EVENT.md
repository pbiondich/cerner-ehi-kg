# CHARGE_EVENT

> Activity table that holds all charging activity. As each charge point is achieved, a 'foreign system' triggers a charge event entry.

**Description:** Charge Event  
**Table type:** ACTIVITY  
**Primary key:** `CHARGE_EVENT_ID`  
**Columns:** 40  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ABN_STATUS_CD` | DOUBLE | NOT NULL |  | This field displays the status of the charge whether it was required, required and missing, or present |
| 2 | `ACCESSION` | VARCHAR(50) |  |  | The accession number assigned to the specimen or case number assigned to the case. |
| 3 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 4 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 5 | `BILL_ITEM_ID` | DOUBLE | NOT NULL |  | The ID of the bill item that will be billed as a result of this charge event. |
| 6 | `CANCELLED_DT_TM` | DATETIME |  |  | Indicates the date and time the order was cancelled. |
| 7 | `CANCELLED_IND` | DOUBLE |  |  | Indicates whether the order was cancelled. |
| 8 | `CHARGE_EVENT_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the charge_event table. It is an internal system assigned number. |
| 9 | `COLLECTION_PRIORITY_CD` | DOUBLE | NOT NULL |  | Value from 2054 that represents the collection priority of the order. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the encounter table. It is an internal system assigned number. |
| 12 | `EPSDT_IND` | DOUBLE |  |  | This field indicates whether or not the patient participates in an EPSDT. EPSDT is an entitlement provided by Medicaid. It is a service available to all individuals age 20 and younger that are eligible for medical assistance through their participating state Medicaid programs. The program includes early detection of illness or defects through regular and periodic screening examinations, follow up care, and promotion of healthy lifestyles. |
| 13 | `EXT_I_EVENT_CONT_CD` | DOUBLE | NOT NULL |  | Value from 13016 that represents from where the ext_i_event_id came ("RESULT ID" for General Lab). |
| 14 | `EXT_I_EVENT_ID` | DOUBLE | NOT NULL |  | The item event id contains the cs_order_id for the careset charge event, order_id for orderables, and a unique id depending on from where the event came (RESULT_ID from General Lab). |
| 15 | `EXT_I_REFERENCE_CONT_CD` | DOUBLE | NOT NULL |  | Value from 13016 that represents "ORD ID". |
| 16 | `EXT_I_REFERENCE_ID` | DOUBLE | NOT NULL |  | TASK_ID from the order. |
| 17 | `EXT_M_EVENT_CONT_CD` | DOUBLE | NOT NULL |  | Value from 13016 that represents "ORD ID". |
| 18 | `EXT_M_EVENT_ID` | DOUBLE | NOT NULL |  | The master event id contains the cs_order_id for caresets or the order_id for regular orderables. This ties back to the order table. |
| 19 | `EXT_M_REFERENCE_CONT_CD` | DOUBLE | NOT NULL |  | Value from 13016 that represents "ORD CAT". |
| 20 | `EXT_M_REFERENCE_ID` | DOUBLE | NOT NULL |  | ID from the order catalog for the ordered item. |
| 21 | `EXT_P_EVENT_CONT_CD` | DOUBLE | NOT NULL |  | The parent event contributor code contains the value from 13016 that represents "ORD ID" for orderables within a careset and children of the orderables within the careset, and zero for the charge event associated with the order. |
| 22 | `EXT_P_EVENT_ID` | DOUBLE | NOT NULL |  | The parent event id contains zero for the charge event associated with the order, the cs_order_id from the order table for orderables within a careset, and the order_id from the order table for the children of the orderables within the careset. |
| 23 | `EXT_P_REFERENCE_CONT_CD` | DOUBLE | NOT NULL |  | The parent event contributor code contains the value from 13016 that represents "ORD CAT" for orderables within a careset and children of the orderables within the careset, and zero for the charge event associated with the order. |
| 24 | `EXT_P_REFERENCE_ID` | DOUBLE | NOT NULL |  | ID from the order catalog for the ordered item for orderables within a careset and children of the orderables within the careset, and zero for the charge event associated with the order. |
| 25 | `HEALTH_PLAN_ID` | DOUBLE | NOT NULL | FK→ | The ID of the health plan associated with the encounter. |
| 26 | `M_BILL_ITEM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the bill_item table for the master (careset) bill item. It is an internal system assigned number. |
| 27 | `M_CHARGE_EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the charge_event table for the master (careset) bill item. It is an internal system assigned number. |
| 28 | `ORDER_ID` | DOUBLE | NOT NULL |  | The order_id from the order table. |
| 29 | `PERF_LOC_CD` | DOUBLE | NOT NULL |  | Value from codeset 220 that represents the locaiton at which the services were provided. |
| 30 | `PERSON_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the person table. It is an internal system assigned number. |
| 31 | `P_BILL_ITEM_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the bill_item table for the parent bill item. It is an internal system assigned number. |
| 32 | `P_CHARGE_EVENT_ID` | DOUBLE | NOT NULL |  | This is the value of the unique primary identifier of the charge_event table for the parent bill item. It is an internal system assigned number. |
| 33 | `REFERENCE_NBR` | VARCHAR(60) |  |  | This value is populated by CSChargeRecovery. The application prompts the user for a reference number when reprocessing missing events. CSChargeRecovery sends the missing events through the AFC Server to be processed. The reference_nbr field is then populated with the reference nbr from the CSChargeRecovery application when the event is reprocessed by the server. |
| 34 | `REPORT_PRIORITY_CD` | DOUBLE | NOT NULL |  | Value from 1905 that represents the reporting priority of the order. |
| 35 | `RESEARCH_ACCOUNT_ID` | DOUBLE | NOT NULL |  | This is the unique identifier to the research_account table. It identifies the research account to be used in charge creation. |
| 36 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 37 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 38 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 39 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 40 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `HEALTH_PLAN_ID` | [HEALTH_PLAN](HEALTH_PLAN.md) | `HEALTH_PLAN_ID` |
| `PERSON_ID` | [PERSON](PERSON.md) | `PERSON_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [CHARGE](CHARGE.md) | `CHARGE_EVENT_ID` |
| [CHARGE_EVENT_ACT](CHARGE_EVENT_ACT.md) | `CHARGE_EVENT_ID` |
| [CHARGE_EVENT_MOD](CHARGE_EVENT_MOD.md) | `CHARGE_EVENT_ID` |
| [UM_CHARGE_EVENT_ST](UM_CHARGE_EVENT_ST.md) | `CHARGE_EVENT_ID` |
| [WORKLOAD](WORKLOAD.md) | `CHARGE_EVENT_ID` |

