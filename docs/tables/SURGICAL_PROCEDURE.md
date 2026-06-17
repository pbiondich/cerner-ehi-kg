# SURGICAL_PROCEDURE

> Contains the attributes of an order catalog entry specific to a surgical procedure

**Description:** Surgical Procedure  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 19

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the order_catalog table indicating the order catalog entry associated with this surgical procedure |
| 2 | `CLEANUP_TIME` | DOUBLE |  |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. Cleanup time required for the procedure in Minutes |
| 3 | `CREATE_APPLCTX` | DOUBLE |  |  | Create Appltication ContextColumn |
| 4 | `CREATE_DT_TM` | DATETIME |  |  | Create Date and TimeColumn |
| 5 | `CREATE_PRSNL_ID` | DOUBLE |  |  | Create Personnel IdColumn |
| 6 | `CREATE_TASK` | DOUBLE |  |  | Create TaskColumn |
| 7 | `DEF_ANESTH_TYPE_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. The default anesthesia type associated with this surgical procedure |
| 8 | `DEF_CASE_LEVEL_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. The default case level associated with this surgical procedure, i.e. Routine 1 Circ 1 Scrub |
| 9 | `DEF_PROC_DUR` | DOUBLE |  |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. The default duration associated with this surgical procedure |
| 10 | `DEF_WOUND_CLASS_CD` | DOUBLE | NOT NULL |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. The default wound class associated with this surgical procedure |
| 11 | `FROZEN_SECTION_REQ_IND` | DOUBLE |  |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. An indicator of whether or not a frozen section is required for this surgical procedure |
| 12 | `SETUP_TIME` | DOUBLE |  |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. Setup Time |
| 13 | `SPEC_REQ_IND` | DOUBLE |  |  | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. An indicator of whether or not a specimen is required for this surgical procedure. This indicator will be used when the Intraoperative Record is being verified. |
| 14 | `SURG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | ** OBSOLETE** This column becomes obsolete when new table SURGE_PROC_DETAIL is implemented. The surgical specialty associated with this surgical procedure. Corresponds to the CDF Meaning of "SURGSPEC" on the prsnl_group table. |
| 15 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 16 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 17 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 18 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 19 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SURG_SPECIALTY_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

