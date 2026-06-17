# RAD_TECH_FMT_ERPRC_R

> The Rad_Tech_Fmt_ErProc_R table holds a relation to a technical comment format and a combination of an exam room and a procedure.

**Description:** Radiology tech comment format and Service resource and procedure relation.  
**Table type:** REFERENCE  
**Primary key:** `FORMAT_ERPRC_RELTN_ID`  
**Columns:** 10  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `CATALOG_CD` | DOUBLE | NOT NULL |  | The Catalog_Cd identifies a procedure that is related to a technical comment format. |
| 2 | `FORMAT_ERPRC_RELTN_ID` | DOUBLE | NOT NULL | PK | The format_ErProc_reltn_Id uniquely identifies a row in the Rad_Tech_Fmt_ErProc_r table. It serves no other purpose other than to uniquely identify the row. |
| 3 | `FORMAT_ID` | DOUBLE | NOT NULL | FK→ | The Format_Id is a foreign key to the Rad_Tech_Format table. It is used to identify a Format. |
| 4 | `SEQUENCE` | DOUBLE | NOT NULL |  | The Sequence identifies an order of fields within a specific format. |
| 5 | `SERVICE_RESOURCE_CD` | DOUBLE | NOT NULL |  | The Service_Resource_Cd identifies a location that is related to a technical comment format. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `FORMAT_ID` | [RAD_TECH_FORMAT](RAD_TECH_FORMAT.md) | `FORMAT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [RAD_TECH_FMT_ERPRC_OVRD](RAD_TECH_FMT_ERPRC_OVRD.md) | `FORMAT_ERPRC_RELTN_ID` |

