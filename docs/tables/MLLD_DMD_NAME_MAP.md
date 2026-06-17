# MLLD_DMD_NAME_MAP

> This table is a staging table used to help facilitate the MLTM tables load process. It is not intended for client use or use by any other process.

**Description:** MLLD_DMD_NAME_MAP  
**Table type:** REFERENCE  
**Primary key:** _(not published — see note)_  
**Columns:** 13

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `APID` | DOUBLE | NOT NULL |  | Identifies An Actual Medicinal Product (AMP). An AMP is a single dose unit of a finished dose form (unless the product is presented as a continuous dosage form), attributable to an identified supplier that contains a specified amount of an ingredient substance. |
| 2 | `APPID` | DOUBLE | NOT NULL |  | Identifies an Actual Medicinal Product Pack (AMPP). An AMPP is the packaged product that is supplied for direct patient use or from which AMPs are supplied for direct patient use. It may contain multiple components each of which may or may not be an AMPP in their own right. |
| 3 | `DMD_NAME` | VARCHAR(255) | NOT NULL |  | The drug name as provided by the dm+d. |
| 4 | `DRUG_SYNONYM_ID` | DOUBLE | NOT NULL | FK→ | this field contains a unique numeric identifier for a description of a drug. |
| 5 | `FUNCTION_ID` | DOUBLE | NOT NULL | FK→ | This field contains the Multum function_id, which is used for determining the type a drug name is. |
| 6 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 7 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 8 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 9 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 10 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 11 | `VPID` | DOUBLE | NOT NULL |  | Identifies A Virtual Medicinal Product (VMP). A VMP is an abstract concept representing the properties of one or more clinically equivalent Actual Medicinal Products, where clinical is defined as relating to the course of a disease. |
| 12 | `VPPID` | DOUBLE | NOT NULL |  | Identifies A Virtual Medicinal Product Pack (VMPP). A VMPP is an abstract concept representing the properties of one or more quantitatively equivalent AMPPs. For every Actual Medicinal Product Pack (AMPP) there will exist a corresponding VMPP. A VMPP will have at least one AMPP and may have many AMPPs linked to it. |
| 13 | `VTMID` | DOUBLE | NOT NULL |  | Identifies a Virtual Therapeutic Moiety (VTM). A VTM is the abstract representation of the substance(s), formulated as a medicinal product, intended by an authorising health care professional for use in the treatment of the patient. |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `DRUG_SYNONYM_ID` | [MLLD_DRUG_NAME](MLLD_DRUG_NAME.md) | `DRUG_SYNONYM_ID` |
| `FUNCTION_ID` | [MLLD_FUNCTION_TYPE](MLLD_FUNCTION_TYPE.md) | `FUNCTION_ID` |

