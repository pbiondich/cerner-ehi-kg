# NOMENCLATURE

> Each row in the Nomenclature table represents a string that appears in a source vocabulary. Any variation in upper-lower case is a separate string.

**Description:** Nomenclature  
**Table type:** REFERENCE  
**Primary key:** `NOMENCLATURE_ID`  
**Columns:** 39  
**Referenced by:** 157 columns

[← index](../index.md)

## Columns

| # | Column | Type | Null? | Flags | Definition |
|--:|--------|------|:-----:|-------|------------|
| 1 | `ACTIVE_IND` | DOUBLE |  |  | The table row is active or inactive. A row is generally active unless it is in an inactive state such as logically deleted, combined away, pending purge, etc. |
| 2 | `ACTIVE_STATUS_CD` | DOUBLE | NOT NULL |  | Indicates the status of the row itself (not the data in the row) such as active, inactive, combined away, pending purge, etc. |
| 3 | `ACTIVE_STATUS_DT_TM` | DATETIME |  |  | The date and time that the active_status_cd was set. |
| 4 | `ACTIVE_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the active_status_cd to be set or change. |
| 5 | `BEG_EFFECTIVE_DT_TM` | DATETIME |  |  | The date and time for which this table row becomes effective. Normally, this will be the date and time the row is added, but could be a past or future date and time. |
| 6 | `CMTI` | VARCHAR(255) |  |  | The Global Unique Identifier from an outside source |
| 7 | `CONCEPT_CKI` | VARCHAR(255) |  |  | Cki from the concept table which is the functional Concept. |
| 8 | `CONCEPT_IDENTIFIER` | VARCHAR(242) |  |  | A unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a concept. All Cerner assigned concept identifiers are created from the CONCEPT_SEQ. The sequence number is formatted to an 8-byte number padded |
| 9 | `CONCEPT_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the concept_identifier. |
| 10 | `CONTRIBUTOR_SYSTEM_CD` | DOUBLE | NOT NULL |  | Contributor system identifies the source feed of data from which a row was populated. This is mainly used to determine how to update a set of data that may have originated from more than one source feed. |
| 11 | `DATA_STATUS_CD` | DOUBLE | NOT NULL |  | Data status indicates a level of authenticity of the row data. Typically this will either be AUTHENTICATED or UNAUTHENTICATED. |
| 12 | `DATA_STATUS_DT_TM` | DATETIME |  |  | The date and time that the data_status_cd was set. |
| 13 | `DATA_STATUS_PRSNL_ID` | DOUBLE | NOT NULL |  | The person who caused the data_status_cd to be set or change. |
| 14 | `DISALLOWED_IND` | DOUBLE | NOT NULL |  | An indicator of whether the term is allowed for selection. |
| 15 | `END_EFFECTIVE_DT_TM` | DATETIME | NOT NULL |  | The date/time after which the row is no longer valid as active current data. This may be valued with the date that the row became inactive. |
| 16 | `LANGUAGE_CD` | DOUBLE | NOT NULL |  | The language that the string is expressed. |
| 17 | `MNEMONIC` | VARCHAR(25) |  |  | A terse description of the source string. |
| 18 | `NOMENCLATURE_ID` | DOUBLE | NOT NULL | PK | This is the value of the unique primary identifier of the nomenclature table. It is an internal system assigned number. |
| 19 | `NOM_VER_GRP_ID` | DOUBLE | NOT NULL | FK→ | Uniquely defines a nomenclature item within the nomenclature table. The nom_ver_grp_id is associated with multiple nomenclature rows. The nom_ver_grp_id is assigned the nomenclature_id when a code is added. All subsequent updates to the code retain the |
| 20 | `PRIMARY_CTERM_IND` | DOUBLE | NOT NULL |  | Identifies the source string as the 'official', primary term. |
| 21 | `PRIMARY_VTERM_IND` | DOUBLE |  |  | Identifies the source_string as the "official", or primary, term for the source_identifier. |
| 22 | `PRINCIPLE_TYPE_CD` | DOUBLE | NOT NULL | FK→ | A general category used to group strings. |
| 23 | `SHORT_STRING` | VARCHAR(60) |  |  | A short description of the source string. |
| 24 | `SOURCE_IDENTIFIER` | VARCHAR(50) |  |  | The code, or key, from the source vocabulary that contributed the string to the nomenclature. |
| 25 | `SOURCE_IDENTIFIER_KEYCAP` | VARCHAR(50) |  |  | The source identifier that is in upper case. |
| 26 | `SOURCE_STRING` | VARCHAR(255) |  |  | Variable length string that may include alphanumeric characters and punctuation. |
| 27 | `SOURCE_STRING_KEYCAP` | VARCHAR(255) |  |  | The source string that is in upper case. |
| 28 | `SOURCE_STRING_KEYCAP_A_NLS` | VARCHAR(1020) |  |  | this field will help facilitate accent insensitive searches/sorts on the SOURCE_STRING_KEYCAP field (National Language Support) |
| 29 | `SOURCE_VOCABULARY_CD` | DOUBLE | NOT NULL |  | The external vocabulary or lexicon that contributed the string, e.g. ICD9, SNOMED, etc. |
| 30 | `STRING_IDENTIFIER` | CHAR(18) |  |  | A unique identifier supplied from Cerner or other external database and is persistent once it is assigned to a string. |
| 31 | `STRING_SOURCE_CD` | DOUBLE | NOT NULL |  | Represents the external source that owns the string_identifier. |
| 32 | `STRING_STATUS_CD` | DOUBLE | NOT NULL |  | An indication of whether the string is the preferred form of a term or a variant of that form, e.g. by case, plurality, word order. |
| 33 | `TERM_ID` | DOUBLE | NOT NULL | FK→ | This is the value of the unique primary identifier of the term table. It is an internal system assigned number. |
| 34 | `UPDT_APPLCTX` | DOUBLE | NOT NULL |  | The application context number from the record info block. |
| 35 | `UPDT_CNT` | DOUBLE | NOT NULL |  | Set to 0 on insert. Incremented by 1 on update. Used to recognize update conflict where data in a row updated by one application is at risk of being lost by a second application attempting to update the row. |
| 36 | `UPDT_DT_TM` | DATETIME | NOT NULL |  | The date and time the row was last inserted or updated. |
| 37 | `UPDT_ID` | DOUBLE | NOT NULL |  | The person_id of the person from the personnel table (prsnl) that caused the last insert or update of the row in the table. |
| 38 | `UPDT_TASK` | DOUBLE | NOT NULL |  | The registered (assigned) task number for the process that inserted or updated the row. |
| 39 | `VOCAB_AXIS_CD` | DOUBLE | NOT NULL | FK→ | Vocabulary AXIS codes related to SNOMEDColumn |

_Flags: PK = primary key · FK→ = published foreign key (see Joins out)._

## Joins out — this table references (published FKs)

| Column | → References | Parent column |
|--------|--------------|---------------|
| `NOM_VER_GRP_ID` | [NOMENCLATURE](NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| `PRINCIPLE_TYPE_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |
| `TERM_ID` | [TERM](TERM.md) | `TERM_ID` |
| `VOCAB_AXIS_CD` | [CODE_VALUE](CODE_VALUE.md) | `CODE_VALUE` |

## Referenced by (157)

| From table | Column |
|------------|--------|
| [ALERT_AUDIT_ALLERGY_DOM](ALERT_AUDIT_ALLERGY_DOM.md) | `NOMENCLATURE_ID` |
| [ALLERGY](ALLERGY.md) | `SUBSTANCE_NOM_ID` |
| [ALLERGY_EXT_DATA](ALLERGY_EXT_DATA.md) | `NOMENCLATURE_ID` |
| [AOAV_CONDITION](AOAV_CONDITION.md) | `NOMENCLATURE_ID` |
| [BATCH_TRANS_FILE](BATCH_TRANS_FILE.md) | `DRG_NOMENCLATURE_ID` |
| [BB_QC_EXPECTED_RESULT_R](BB_QC_EXPECTED_RESULT_R.md) | `NOMENCLATURE_ID` |
| [BB_QC_RESULT](BB_QC_RESULT.md) | `NOMENCLATURE_ID` |
| [BB_RH_PHENOTYPE](BB_RH_PHENOTYPE.md) | `FR_NOMENCLATURE_ID` |
| [BB_RH_PHENOTYPE](BB_RH_PHENOTYPE.md) | `W_NOMENCLATURE_ID` |
| [BMDI_DEVICE_NOMENCLATURE](BMDI_DEVICE_NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| [BT_COND_CRIT_GRP_RELTN](BT_COND_CRIT_GRP_RELTN.md) | `NOMENCLATURE_ID` |
| [CAC_NOMENCLATURE](CAC_NOMENCLATURE.md) | `MAPPED_NOMENCLATURE_ID` |
| [CAC_NOMENCLATURE](CAC_NOMENCLATURE.md) | `NOMENCLATURE_ID` |
| [CHARGE](CHARGE.md) | `ALPHA_NOMEN_ID` |
| [CHARGE_EVENT_ACT](CHARGE_EVENT_ACT.md) | `ALPHA_NOMEN_ID` |
| [CNT_DCP_INTERP_STATE](CNT_DCP_INTERP_STATE.md) | `NOMENCLATURE_ID` |
| [CNT_DCP_INTERP_STATE](CNT_DCP_INTERP_STATE.md) | `RESULT_NOMENCLATURE_ID` |
| [CONCEPT_PRSNL_CROSSMAP](CONCEPT_PRSNL_CROSSMAP.md) | `SOURCE_NOMEN_ID` |
| [CONCEPT_PRSNL_CROSSMAP](CONCEPT_PRSNL_CROSSMAP.md) | `TARGET_NOMEN_ID` |
| [CV_CASE_ABSTR_DATA](CV_CASE_ABSTR_DATA.md) | `NOMENCLATURE_ID` |
| [CV_DEV_ABSTR_DATA](CV_DEV_ABSTR_DATA.md) | `NOMENCLATURE_ID` |
| [CYTO_STANDARD_RPT_R](CYTO_STANDARD_RPT_R.md) | `NOMENCLATURE_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `MOD_NOMENCLATURE_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `NOMENCLATURE_ID` |
| [DIAGNOSIS](DIAGNOSIS.md) | `ORIGINATING_NOMENCLATURE_ID` |
| [DIAGNOSIS_HIST](DIAGNOSIS_HIST.md) | `NOMENCLATURE_ID` |
| [DRG](DRG.md) | `NOMENCLATURE_ID` |
| [DRG_SPECIALTY](DRG_SPECIALTY.md) | `NOMENCLATURE_ID` |
| [DSM_COMPONENT](DSM_COMPONENT.md) | `NOMENCLATURE_ID` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `DIAG_NOMEN_ID` |
| [EEM_ABN_CHECK](EEM_ABN_CHECK.md) | `PROC_NOMEN_ID` |
| [EEM_ABN_DIAG](EEM_ABN_DIAG.md) | `DIAG_NOMEN_ID` |
| [EEM_ABN_MOD](EEM_ABN_MOD.md) | `MOD_NOMEN_ID` |
| [EEM_BENEFIT_QUAL](EEM_BENEFIT_QUAL.md) | `BEG_NOMEN_ID` |
| [EEM_BENEFIT_QUAL](EEM_BENEFIT_QUAL.md) | `END_NOMEN_ID` |
| [EEM_SERVICE_LIST](EEM_SERVICE_LIST.md) | `CAUSE_BEG_NOMEN_ID` |
| [EEM_SERVICE_LIST](EEM_SERVICE_LIST.md) | `CAUSE_END_NOMEN_ID` |
| [EEM_SERVICE_LIST](EEM_SERVICE_LIST.md) | `TYPE_BEG_NOMEN_ID` |
| [EEM_SERVICE_LIST](EEM_SERVICE_LIST.md) | `TYPE_END_NOMEN_ID` |
| [ENCNTR_INFO](ENCNTR_INFO.md) | `VALUE_NOMENCLATURE_ID` |
| [ENCNTR_INFO_HIST](ENCNTR_INFO_HIST.md) | `VALUE_NOMENCLATURE_ID` |
| [ENCNTR_PLAN_ELIGIBILITY](ENCNTR_PLAN_ELIGIBILITY.md) | `PROC_NOMEN_ID` |
| [EXPEDITE_CODED_RESP](EXPEDITE_CODED_RESP.md) | `NOMENCLATURE_ID` |
| [FHX_ACTIVITY](FHX_ACTIVITY.md) | `NOMENCLATURE_ID` |
| [FHX_SECTION_DEF](FHX_SECTION_DEF.md) | `NOMENCLATURE_ID` |
| [FILL_PRINT_ORD_HX](FILL_PRINT_ORD_HX.md) | `ICD9_ID` |
| [FN_EV_SURVEY_ELEMENT_ACT](FN_EV_SURVEY_ELEMENT_ACT.md) | `NOMENCLATURE_ID` |
| [FN_EV_SURVEY_ELEMENT_REF](FN_EV_SURVEY_ELEMENT_REF.md) | `NOMENCLATURE_ID` |
| [HEALTH_CONCERN](HEALTH_CONCERN.md) | `NOMENCLATURE_ID` |
| [HIM_HAC_CRITERIA](HIM_HAC_CRITERIA.md) | `COMPARE_DX_NOMEN_ID` |
| [HIM_HAC_CRITERIA](HIM_HAC_CRITERIA.md) | `COMPARE_PX_NOMEN_ID` |
| [HIM_HAC_CRITERIA](HIM_HAC_CRITERIA.md) | `HAC_NOMENCLATURE_ID` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `DILUTION_NOM_ID` |
| [HLA_AB_SCREEN_HISTORY_MAP](HLA_AB_SCREEN_HISTORY_MAP.md) | `METHODOLOGY_NOM_ID` |
| [HLA_NOMEN_CODE_R](HLA_NOMEN_CODE_R.md) | `NOMENCLATURE_ID` |
| [HLA_XM_HISTORY_MAP](HLA_XM_HISTORY_MAP.md) | `XM_TYPE_NOM_ID` |
| [HM_EXPECT_SAT](HM_EXPECT_SAT.md) | `NOMENCLATURE_ID` |
| [HM_EXPECT_SAT_HIST](HM_EXPECT_SAT_HIST.md) | `NOMENCLATURE_ID` |
| [IB_RX_REQ_DIAGNOSIS](IB_RX_REQ_DIAGNOSIS.md) | `NOMENCLATURE_ID` |
| [IMPLANT_HISTORY](IMPLANT_HISTORY.md) | `PROCEDURE_NOMEN_ID` |
| [INTERP_RESULT](INTERP_RESULT.md) | `RESULT_NOMENCLATURE_ID` |
| [LH_CNT_LTD_DATA_DETAIL](LH_CNT_LTD_DATA_DETAIL.md) | `NOMEN_ID` |
| [MEDICATION_DEFINITION](MEDICATION_DEFINITION.md) | `MDX_GFC_NOMEN_ID` |
| [NOMENCLATURE](NOMENCLATURE.md) | `NOM_VER_GRP_ID` |
| [NOMENCLATURE_ENCNTR_DESC](NOMENCLATURE_ENCNTR_DESC.md) | `NOMENCLATURE_ID` |
| [NOMENCLATURE_OUTBOUND](NOMENCLATURE_OUTBOUND.md) | `NOMENCLATURE_ID` |
| [NOMEN_ENTITY_RELTN](NOMEN_ENTITY_RELTN.md) | `NOMENCLATURE_ID` |
| [NOMEN_GROUP_RELTN](NOMEN_GROUP_RELTN.md) | `NOMEN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `DRG_NOMEN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `ICD9_ADMIT_DIAG_NOMEN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `ICD9_PRIN_DIAG_NOMEN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `ICD9_PRIN_PROC_NOMEN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `ICD9_SECONDARY1_DIAG_NOMEN_ID` |
| [OMF_ENCNTR_ST](OMF_ENCNTR_ST.md) | `MRD_NOMEN_ID` |
| [ONC_MTUITIVE_WORKSHEET](ONC_MTUITIVE_WORKSHEET.md) | `NOMENCLATURE_ID` |
| [ONC_NOMEN_DOCSETREF_R](ONC_NOMEN_DOCSETREF_R.md) | `NOMENCLATURE_ID` |
| [ONC_NOMEN_TERM_RELTN](ONC_NOMEN_TERM_RELTN.md) | `NOMENCLATURE_ID` |
| [ORDER_POTENTIAL_DIAGNOSIS](ORDER_POTENTIAL_DIAGNOSIS.md) | `NOMENCLATURE_ID` |
| [ORDER_POTENTIAL_DIAGNOSIS](ORDER_POTENTIAL_DIAGNOSIS.md) | `ORIGINATING_NOMENCLATURE_ID` |
| [OUTCOME_CAT_CRITERIA](OUTCOME_CAT_CRITERIA.md) | `NOMENCLATURE_ID` |
| [OUTCOME_CRITERIA](OUTCOME_CRITERIA.md) | `NOMENCLATURE_ID` |
| [PDOC_ASSESSPLAN_CONTENT](PDOC_ASSESSPLAN_CONTENT.md) | `NOMENCLATURE_ID` |
| [PERFORM_RESULT](PERFORM_RESULT.md) | `NOMENCLATURE_ID` |
| [PERSON_HLA_AB_SCN_AUDIT](PERSON_HLA_AB_SCN_AUDIT.md) | `DILUTION_NOM_ID` |
| [PERSON_HLA_AB_SCN_AUDIT](PERSON_HLA_AB_SCN_AUDIT.md) | `METHODOLOGY_NOM_ID` |
| [PERSON_HLA_AB_SCN_AUDIT](PERSON_HLA_AB_SCN_AUDIT.md) | `REACTION_NOM_ID` |
| [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `DILUTION_NOM_ID` |
| [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `METHODOLOGY_NOM_ID` |
| [PERSON_HLA_AB_SCREEN](PERSON_HLA_AB_SCREEN.md) | `REACTION_NOM_ID` |
| [PERSON_HLA_AB_SPEC](PERSON_HLA_AB_SPEC.md) | `HLA_TYPE_NOM_ID` |
| [PERSON_HLA_TYPE](PERSON_HLA_TYPE.md) | `HLA_TYPE_NOM_ID` |
| [PERSON_HLA_TYPE_AUDIT](PERSON_HLA_TYPE_AUDIT.md) | `HLA_TYPE_NOM_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `B_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `MONO_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `TB_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `T_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM](PERSON_HLA_XM.md) | `XM_TYPE_NOM_ID` |
| [PERSON_HLA_XM_AUDIT](PERSON_HLA_XM_AUDIT.md) | `B_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM_AUDIT](PERSON_HLA_XM_AUDIT.md) | `MONO_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM_AUDIT](PERSON_HLA_XM_AUDIT.md) | `TB_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM_AUDIT](PERSON_HLA_XM_AUDIT.md) | `T_CELL_RESULT_NOM_ID` |
| [PERSON_HLA_XM_AUDIT](PERSON_HLA_XM_AUDIT.md) | `XM_TYPE_NOM_ID` |
| [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `EMPL_OCCUPATION_NOMEN_ID` |
| [PERSON_ORG_RELTN](PERSON_ORG_RELTN.md) | `EMPL_OCC_INDUSTRY_NOMEN_ID` |
| [PERSON_ORG_RELTN_HIST](PERSON_ORG_RELTN_HIST.md) | `EMPL_OCCUPATION_NOMEN_ID` |
| [PERSON_ORG_RELTN_HIST](PERSON_ORG_RELTN_HIST.md) | `EMPL_OCC_INDUSTRY_NOMEN_ID` |
| [PERSON_RH_PHENO_RESULT](PERSON_RH_PHENO_RESULT.md) | `NOMENCLATURE_ID` |
| [PERSON_TRIBAL_AFLTN](PERSON_TRIBAL_AFLTN.md) | `TRIBAL_ENTITY_NOMENCLATURE_ID` |
| [PERSON_TRIBAL_AFLTN_HIST](PERSON_TRIBAL_AFLTN_HIST.md) | `TRIBAL_ENTITY_NOMENCLATURE_ID` |
| [PFT_CHARGE_GLOBAL_DAYS](PFT_CHARGE_GLOBAL_DAYS.md) | `MOD_NOMEN_ID` |
| [PFT_CHARGE_GLOBAL_DAYS](PFT_CHARGE_GLOBAL_DAYS.md) | `PROC_NOMEN_ID` |
| [PFT_CM_EVENT_LOG](PFT_CM_EVENT_LOG.md) | `NOMENCLATURE_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `CPT_NOMEN_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `DRG_NOMEN_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `HCPCS_NOMEN_ID` |
| [PFT_REVENUE_SUMMARY](PFT_REVENUE_SUMMARY.md) | `ICD9_NOMEN_ID` |
| [PFT_RVU_CONTENT](PFT_RVU_CONTENT.md) | `MOD_NOMEN_ID` |
| [PFT_RVU_CONTENT](PFT_RVU_CONTENT.md) | `PROC_NOMEN_ID` |
| [PHA_DISP_OBS_ST](PHA_DISP_OBS_ST.md) | `ICD9_NOMEN_ID` |
| [PHA_ORD_ACT_OBS_ST](PHA_ORD_ACT_OBS_ST.md) | `ICD9_NOMEN_ID` |
| [PHA_PROD_DISP_OBS_ST](PHA_PROD_DISP_OBS_ST.md) | `ICD9_NOMEN_ID` |
| [PI_LEAFLET](PI_LEAFLET.md) | `NOMENCLATURE_ID` |
| [PL_PC_ORG_DIAG_XREF](PL_PC_ORG_DIAG_XREF.md) | `NOMENCLATURE_ID` |
| [PROBLEM](PROBLEM.md) | `NOMENCLATURE_ID` |
| [PROBLEM](PROBLEM.md) | `ORIGINATING_NOMENCLATURE_ID` |
| [PROBLEM_EXT_DATA](PROBLEM_EXT_DATA.md) | `ORIGINATING_NOMENCLATURE_ID` |
| [PROBLEM_EXT_DATA](PROBLEM_EXT_DATA.md) | `TARGET_NOMENCLATURE_ID` |
| [PROCEDURE](PROCEDURE.md) | `DIAG_NOMENCLATURE_ID` |
| [PROCEDURE](PROCEDURE.md) | `MOD_NOMENCLATURE_ID` |
| [PROCEDURE](PROCEDURE.md) | `NOMENCLATURE_ID` |
| [PROCEDURE_EXT_DATA](PROCEDURE_EXT_DATA.md) | `NOMENCLATURE_ID` |
| [PROCEDURE_HIST](PROCEDURE_HIST.md) | `NOMENCLATURE_ID` |
| [PROP_RESULT](PROP_RESULT.md) | `NOMENCLATURE_ID` |
| [PT_PROT_REG](PT_PROT_REG.md) | `NOMENCLATURE_ID` |
| [QC_RESULT](QC_RESULT.md) | `NOMENCLATURE_ID` |
| [RCR_TRANS_DIST](RCR_TRANS_DIST.md) | `NOMENCLATURE_ID` |
| [REF_CD_MAP_DETAIL](REF_CD_MAP_DETAIL.md) | `NOMENCLATURE_ID` |
| [RESULT_HASH](RESULT_HASH.md) | `NOMENCLATURE_ID` |
| [SA_ANESTHESIA_REC_FIELD_VALUES](SA_ANESTHESIA_REC_FIELD_VALUES.md) | `DIAGNOSIS_NOMENCLATURE_ID` |
| [SA_ANESTHESIA_REC_FIELD_VALUES](SA_ANESTHESIA_REC_FIELD_VALUES.md) | `PROBLEM_NOMENCLATURE_ID` |
| [SA_ANESTHESIA_REC_FIELD_VALUES](SA_ANESTHESIA_REC_FIELD_VALUES.md) | `PROCEDURE_NOMENCLATURE_ID` |
| [SA_PARAMETER_VALUE](SA_PARAMETER_VALUE.md) | `NOMENCLATURE_ID` |
| [SCH_ABN_CROSS](SCH_ABN_CROSS.md) | `PROC_NOMEN_ID` |
| [SCH_NOMEN_LIST](SCH_NOMEN_LIST.md) | `BEG_NOMENCLATURE_ID` |
| [SCH_NOMEN_LIST](SCH_NOMEN_LIST.md) | `END_NOMENCLATURE_ID` |
| [SHX_ALPHA_RESPONSE](SHX_ALPHA_RESPONSE.md) | `NOMENCLATURE_ID` |
| [SN_NOMEN_ST](SN_NOMEN_ST.md) | `NOMENCLATURE_ID` |
| [SN_PROC_CPT_R](SN_PROC_CPT_R.md) | `NOMENCLATURE_ID` |
| [SN_SURG_CASE_PROC_CPT](SN_SURG_CASE_PROC_CPT.md) | `NOMENCLATURE_ID` |
| [UCMR_KARYOTYPE_CONCEPT](UCMR_KARYOTYPE_CONCEPT.md) | `NOMENCLATURE_ID` |
| [UCM_KARYOTYPE_CONCEPT](UCM_KARYOTYPE_CONCEPT.md) | `NOMENCLATURE_ID` |
| [UKR_SACT](UKR_SACT.md) | `NOMENCLATURE_ID` |
| [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `APPLIED_CHARGE_ID` |
| [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `APPLIED_MODIFIER_ID` |
| [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `PRIMARY_NOMENCLATURE_ID` |
| [VISITCODING_AUDIT](VISITCODING_AUDIT.md) | `SUGGESTED_CHARGE_ID` |
| [VISITCODING_DX](VISITCODING_DX.md) | `NOMENCLATURE_ID` |

