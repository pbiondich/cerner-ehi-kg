# SURG_PROC_DETAIL

> Contains the default attributes associated with a surgical procedure for a specific surgical area.

**Description:** Surgical Procedure Detail  
**Table type:** REFERENCE  
**Primary key:** `SURG_PROC_DETAIL_ID`  
**Columns:** 24  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ANESTHESIA_TYPE_CD` | DOUBLE | NOT NULL |  | The default anesthesia type associated with this surgical procedure and area. |
| 2 | `BLOOD_PRODUCT_REQ_IND` | DOUBLE | NOT NULL |  | An indicator of whether blood products are required for this surgical procedure and area. |
| 3 | `CASE_LEVEL_CD` | DOUBLE | NOT NULL |  | The default case level (such as Routine 1 Circ 1 Scrub) associated with this procedure and area. |
| 4 | `CATALOG_CD` | DOUBLE | NOT NULL | FK→ | A reference (foreign key) to the ORDER_CATALOG table indicating the order catalog entry associated with this surgical procedure. |
| 5 | `FROZEN_SECTION_REQ_IND` | DOUBLE | NOT NULL |  | An indicator of whether a frozen section is required for this surgical procedure and area. |
| 6 | `IMPLANT_IND` | DOUBLE | NOT NULL |  | An indicator of whether an implant is required for this surgical procedure and area. |
| 7 | `PROC_CNT` | DOUBLE | NOT NULL |  | The number of procedures that are actually represented by this surgical procedure and area. If this is a combination of procedures, this will be greater than one. |
| 8 | `SPEC_REQ_IND` | DOUBLE | NOT NULL |  | An indicator of whether a specimen is required for this surgical procedure and area. This indicator will be used when the Intraoperative Record is being verified. |
| 9 | `SURG_AREA_CD` | DOUBLE | NOT NULL |  | The surgical area associated with this procedure. |
| 10 | `SURG_PROC_DETAIL_ID` | DOUBLE | NOT NULL | PK | The Primary Key, uniquely identifying a procedure / area relation. |
| 11 | `SURG_SPECIALTY_ID` | DOUBLE | NOT NULL | FK→ | Surgical Specialty ID. FK from PRSNL_GROUP. |
| 12 | `UD1_CD` | DOUBLE | NOT NULL |  | This is a user-defined, codified default for this surgical procedure and area. |
| 13 | `UD2_CD` | DOUBLE | NOT NULL |  | This is a user-defined, codified default for this surgical procedure and area. |
| 14 | `UD3_CD` | DOUBLE | NOT NULL |  | This is a user-defined, codified default for this surgical procedure and area. |
| 15 | `UD4_CD` | DOUBLE | NOT NULL |  | This is a user-defined, codified default for this surgical procedure and area. |
| 16 | `UD5_CD` | DOUBLE | NOT NULL |  | This is a user-defined, codified default for this surgical procedure and area. |
| 17 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 18 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 19 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 20 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 21 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 22 | `WOUND_CLASS_CD` | DOUBLE | NOT NULL |  | The default wound class associated with this procedure and area. |
| 23 | `XRAY_IND` | DOUBLE | NOT NULL |  | An indicator of whether an Xray is required for this surgical procedure and area. |
| 24 | `XRAY_TECH_IND` | DOUBLE | NOT NULL |  | An indicator of whether an Xray technician is required for this surgical procedure and area. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `CATALOG_CD` | [ORDER_CATALOG](ORDER_CATALOG.md) | `CATALOG_CD` |
| `SURG_SPECIALTY_ID` | [PRSNL_GROUP](PRSNL_GROUP.md) | `PRSNL_GROUP_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [SURG_PROC_DURATION](SURG_PROC_DURATION.md) | `SURG_PROC_DETAIL_ID` |

