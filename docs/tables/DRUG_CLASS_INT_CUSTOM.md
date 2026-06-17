# DRUG_CLASS_INT_CUSTOM

> Store identifiers for class to class, class to drug custom interactions.

**Description:** DRUG CLASS CUSTOM INTERACTIONS  
**Table type:** REFERENCE  
**Primary key:** `DRUG_CLASS_INT_CUSTOM_ID`  
**Columns:** 14  
**Referenced by:** 1 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `COMBO_IND` | DOUBLE | NOT NULL |  | This would store 0 or 1 to represent the customization includes combination drugs (1) or not (0) |
| 2 | `CUSTOM_INTERACTION_FLAG` | DOUBLE | NOT NULL |  | Custom Interaction type. 1 - Drug/Drug Interaction 2 - Drug/Allergy Interaction 3 - Drug/Food Interaction 4 - Duplicate Therapy Interaction |
| 3 | `CUSTOM_TYPE_FLAG` | DOUBLE | NOT NULL |  | CUSTOM TYPE FLAG - 0 - dnum to dnum 1 - class to dnum 2 - class to class |
| 4 | `DRUG_CLASS_INT_CUSTOM_ID` | DOUBLE | NOT NULL | PK | PRIMARY KEY |
| 5 | `ENTITY1_DISPLAY` | VARCHAR(255) | NOT NULL |  | DISPLAY FIELD TEXT |
| 6 | `ENTITY1_IDENT` | VARCHAR(40) | NOT NULL |  | Entity Identifier 1 |
| 7 | `ENTITY2_DISPLAY` | VARCHAR(255) | NOT NULL |  | DISPLAY FIELD TEXT |
| 8 | `ENTITY2_IDENT` | VARCHAR(40) | NOT NULL |  | Entity Identifier 2 |
| 9 | `LONG_TEXT_ID` | DOUBLE | NOT NULL | FK→ | FK value from the LONG_TEXT table |
| 10 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 11 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 12 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 13 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 14 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `LONG_TEXT_ID` | [LONG_TEXT](LONG_TEXT.md) | `LONG_TEXT_ID` |

## Referenced by (1)

| From table | Column |
|------------|--------|
| [DRUG_CLASS_INT_CSTM_ENTITY_R](DRUG_CLASS_INT_CSTM_ENTITY_R.md) | `DRUG_CLASS_INT_CUSTOM_ID` |

