# ENCNTR_PROCEDURE

> Contains the planned procedures for an encounters

**Description:** Encounter Procedure Table  
**Table type:** ACTIVITY  
**Primary key:** _(not published — see note)_  
**Columns:** 26

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | Order catalog code planned for an encounter. |
| 2 | `CONCURRENT_IND` | DOUBLE | NOT NULL |  | Concurrent Indicator - Specifies that the procedure is concurrent with the previous procedure in the sequence. |
| 3 | `ENCNTR_ID` | DOUBLE | NOT NULL | FK→ | Encounter which the planned procedures are for. |
| 4 | `ENCNTR_PROCEDURE_ID` | DOUBLE | NOT NULL |  | Unique identifier for the Encntr_procedure table. |
| 5 | `NCEPOD_CD` | DOUBLE | NOT NULL |  | The NCEPOD (National Confidential Enquiry into Patient Outcome and Death) Classification categorizes the urgency of the patient's intervention. |
| 6 | `PRIORITY_SEQ` | DOUBLE | NOT NULL |  | Priority of the order. 0 = primary, 1 = secondary, etc. |
| 7 | `PROC_START_DT_TM` | DATETIME |  |  | The start time for the procedure. |
| 8 | `PROC_TEXT` | VARCHAR(255) |  |  | Comments about the procedure. |
| 9 | `SCHED_ANESTH_TYPE_CD` | DOUBLE | NOT NULL |  | The default anesthesia type associated with this surgical procedure and area. |
| 10 | `SCHED_DUR` | DOUBLE | NOT NULL |  | The scheduled length of the procedure. |
| 11 | `SCHED_PRIMARY_IND` | DOUBLE | NOT NULL |  | Used for Surgery Management Reporting. Indicates whether this procedure was scheduled as the primary procedure. |
| 12 | `SCHED_PRIMARY_SURGEON_ID` | DOUBLE | NOT NULL | FK→ | The ID of the primary surgeon scheduled for this procedure. Associated to a row on the PRSNL table. |
| 13 | `SCHED_PRIORITY_CD` | DOUBLE | NOT NULL |  | The priority of the scheduled procedure. Some examples are rush, stat, routine, etc. |
| 14 | `SCHED_SURGE_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this procedure. |
| 15 | `SCHED_SURGICAL_MOD1_CD` | DOUBLE | NOT NULL |  | Stores Surgical Procedure modifiers are used to describe the procedure location/procedure attributes. An example would be left, deep, inner, etc. Each procedure can have multiple descriptions. |
| 16 | `SCHED_SURGICAL_MOD2_CD` | DOUBLE | NOT NULL |  | Stores Surgical Procedure modifiers are used to describe the procedure location/procedure attributes. An example would be left, deep, inner, etc. Each procedure can have multiple descriptions. |
| 17 | `SCHED_SURGICAL_MOD3_CD` | DOUBLE | NOT NULL |  | Stores Surgical Procedure modifiers are used to describe the procedure location/procedure attributes. An example would be left, deep, inner, etc. Each procedure can have multiple descriptions. |
| 18 | `SCHED_SURGICAL_ORDER_COMMENT` | VARCHAR(255) |  |  | Stores comments about surgical orders. |
| 19 | `SCHED_XRAY_IND` | DOUBLE | NOT NULL |  | An indicator of whether an x-ray is required for this surgical procedure and area. |
| 20 | `SCHED_XRAY_TECH_IND` | DOUBLE | NOT NULL |  | An indicator of whether an Xray technician is required for this surgical procedure and area. |
| 21 | `SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | The order synonym associated to the procedure. |
| 22 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 23 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 24 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 25 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 26 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `ENCNTR_ID` | [ENCOUNTER](ENCOUNTER.md) | `ENCNTR_ID` |
| `SCHED_PRIMARY_SURGEON_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SYNONYM_ID` | [ORDER_CATALOG_SYNONYM](ORDER_CATALOG_SYNONYM.md) | `SYNONYM_ID` |

