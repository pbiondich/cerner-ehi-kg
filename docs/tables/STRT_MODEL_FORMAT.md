# STRT_MODEL_FORMAT

> Identifies which format should be used for a model by a version number

**Description:** Starter Model Format  
**Table type:** REFERENCE  
**Primary key:** `STRT_MODEL_FORMAT_ID`  
**Columns:** 9  
**Referenced by:** 2 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `MODEL_VERSION` | DOUBLE | NOT NULL |  | Identifies starter model version |
| 2 | `RESULT_FORMAT_CD` | DOUBLE | NOT NULL |  | Identifies the format that will be used for packaging results |
| 3 | `STRT_MODEL_FORMAT_ID` | DOUBLE | NOT NULL | PK | Unique identifier to be used as a primary key for this table. |
| 4 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | FK→ | Identifies starter model. |
| 5 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 6 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 7 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 8 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 9 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `STRT_MODEL_ID` | [STRT_MODEL](STRT_MODEL.md) | `STRT_MODEL_ID` |

## Referenced by (2)

| From table | Column |
|------------|--------|
| [DEVICE_HL7_MAP](DEVICE_HL7_MAP.md) | `STRT_MODEL_FORMAT_ID` |
| [STRT_MODEL_HL7_MAP](STRT_MODEL_HL7_MAP.md) | `STRT_MODEL_FORMAT_ID` |

