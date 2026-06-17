# SN_PICKLIST

> Picklist for specific document type for a surgical case

**Description:** SURGINET PICKLIST  
**Table type:** ACTIVITY  
**Primary key:** `SN_PICKLIST_ID`  
**Columns:** 12  
**Referenced by:** 5 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `DOC_TYPE_CD` | DOUBLE | NOT NULL |  | The document type for the surgical case the picklist is associated to |
| 2 | `GENERATED_DT_TM` | DATETIME |  |  | The Date/Time that the picklist was last generated |
| 3 | `OPTIMIZED_DT_TM` | DATETIME |  |  | The identifier of the user who last optimized the picklist |
| 4 | `OPTIMIZED_PRSNL_ID` | DOUBLE | NOT NULL | FK→ | The identifier of the user who last optimized the picklist |
| 5 | `REGENERATED_IND` | DOUBLE | NOT NULL |  | indicates the picklist has be regenerated after the picking process has begun |
| 6 | `SN_PICKLIST_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 7 | `SURG_CASE_ID` | DOUBLE | NOT NULL | FK→ | Surigcal Case the picklist is associated to |
| 8 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 9 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 10 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 11 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |
| 12 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. The UPDT family of columns are typically used for housekeeping and external system process and should never be depended on for solution specific logic. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `OPTIMIZED_PRSNL_ID` | [PRSNL](PRSNL.md) | `PERSON_ID` |
| `SURG_CASE_ID` | [SURGICAL_CASE](SURGICAL_CASE.md) | `SURG_CASE_ID` |

## Referenced by (5)

| From table | Column |
|------------|--------|
| [SN_PICKLIST_ITEM](SN_PICKLIST_ITEM.md) | `SN_PICKLIST_ID` |
| [SN_PICKLIST_LOCK](SN_PICKLIST_LOCK.md) | `SN_PICKLIST_ID` |
| [SN_PICKLIST_LOC_STATUS](SN_PICKLIST_LOC_STATUS.md) | `SN_PICKLIST_ID` |
| [SN_PICKLIST_PREF_CARD_R](SN_PICKLIST_PREF_CARD_R.md) | `SN_PICKLIST_ID` |
| [SN_PICKLIST_STATUS](SN_PICKLIST_STATUS.md) | `SN_PICKLIST_ID` |

