# STRT_MODEL

> Stores a description, name, program name for each model.

**Description:** Stores a list of all laboratory analyzer models that Cerner has an interface for  
**Table type:** REFERENCE  
**Primary key:** `STRT_MODEL_ID`  
**Columns:** 15  
**Referenced by:** 13 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DESCRIPTION` | VARCHAR(100) |  |  | Contains a laboratory analyzer's specific model name. |
| 2 | `DEVICE_CATEGORY_CD` | DOUBLE | NOT NULL |  | Category of the bedside medical device - monitor, ventilator, pump etc. |
| 3 | `DEVICE_CATEGORY_TYPE_CD` | DOUBLE | NOT NULL |  | Category type of the bedside medical device - heart monitor, fetal monitor etc. |
| 4 | `ID_TYPE` | CHAR(1) |  |  | Contains micro id type of "A" or "N" to indicate if a micro analyzer accepts an alpha/numeric or just numeric identifier, respectively. |
| 5 | `INTFC_PROGNAME` | CHAR(15) |  |  | Contains the interface program name used by the model. |
| 6 | `ISOLATE_NUMBER_SIZE` | CHAR(1) |  |  | Contains the maximum number of characters a micro analyzer can use for it's isolate number. |
| 7 | `LAB_TYPE` | CHAR(5) |  |  | Contains a character indication the lab type of the model either General Lab or Microbiology. |
| 8 | `MAX_ID_SIZE` | DOUBLE |  |  | This field sets the maximum id size that an analyzer may send. |
| 9 | `STRT_MODEL_CD` | DOUBLE | NOT NULL |  | This value is used to standardize Model information across systems. |
| 10 | `STRT_MODEL_ID` | DOUBLE | NOT NULL | PK | Key field. Contains a DBMS assigned value as the unique key. |
| 11 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 12 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 13 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 14 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 15 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Referenced by (13)

| From table | Column |
|------------|--------|
| [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `STRT_MODEL_CHILD_ID` |
| [BMDI_MONITORED_DEVICE](BMDI_MONITORED_DEVICE.md) | `STRT_MODEL_ID` |
| [LAB_INSTRUMENT](LAB_INSTRUMENT.md) | `STRT_MODEL_ID` |
| [STRT_BMDI_MODEL_NOMENCLATURE](STRT_BMDI_MODEL_NOMENCLATURE.md) | `STRT_MODEL_ID` |
| [STRT_BMDI_MODEL_PARAMETER](STRT_BMDI_MODEL_PARAMETER.md) | `STRT_MODEL_ID` |
| [STRT_MFG_MODEL_R](STRT_MFG_MODEL_R.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_ASSAY_ALIAS](STRT_MODEL_ASSAY_ALIAS.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_ASSAY_R](STRT_MODEL_ASSAY_R.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_CUSTOM](STRT_MODEL_CUSTOM.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_FORMAT](STRT_MODEL_FORMAT.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_HL7_MAP](STRT_MODEL_HL7_MAP.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_LAB_TYPE_R](STRT_MODEL_LAB_TYPE_R.md) | `STRT_MODEL_ID` |
| [STRT_MODEL_SUB_FIELD](STRT_MODEL_SUB_FIELD.md) | `STRT_MODEL_ID` |

